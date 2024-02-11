-- Q2
SELECT count(distinct PULocationID) FROM `terraform-course-411914.taxi.green_taxi_2022`;

SELECT count(distinct PULocationID) FROM `terraform-course-411914.taxi.green_taxi_2022_ext`;

-- Q3
SELECT count(*) FROM `terraform-course-411914.taxi.green_taxi_2022` where fare_amount = 0;

-- Q4
CREATE OR REPLACE TABLE `terraform-course-411914.taxi.green_taxi_2022_part`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM `terraform-course-411914.taxi.green_taxi_2022`;

-- Q5
SELECT DISTINCT PUlocationID FROM `terraform-course-411914.taxi.green_taxi_2022`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

SELECT DISTINCT PUlocationID FROM `terraform-course-411914.taxi.green_taxi_2022_part`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';