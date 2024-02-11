#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine

import os
import argparse

def main(params):

    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = 'outputcsv.csv'

    os.system(f"wget {url} -O {csv_name}.gz")
    os.system(f"gzip -d {csv_name}.gz")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    df.head(0).to_sql(con = engine, name=table_name, if_exists='replace')

    df.to_sql(con = engine, name=table_name, if_exists='append')

    while True:
        df = next(df_iter)

        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

        df.to_sql(con = engine, name=table_name, if_exists='append')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to postgress')
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)