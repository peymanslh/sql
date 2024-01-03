---
title: "WHERE"
date: 2023-12-30T23:17:01+03:30
tags:
- query
- postgresql
---
With `WHERE` we can add a condition to our queries and filter the
output based on that condition.
```sql
-- get user with email of rmcconnell@yahoo.com
SELECT
  first_name, last_name, email
FROM users
WHERE email = 'rmcconnell@yahoo.com';
-- +------------+-----------+----------------------+
-- | first_name | last_name | email                |
-- |------------+-----------+----------------------|
-- | Carmen     | Malone    | rmcconnell@yahoo.com |
-- +------------+-----------+----------------------+

-- get all orders by a user with id of 480
SELECT *
FROM orders
WHERE user_id = 480;
-- +-----+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------+
-- | id  | created_at          | order_code                           | product_id | user_id | quantity | total_price | delivered |
-- |-----+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------|
-- | 1   | 2022-10-08 17:50:42 | 28e9fe61-8883-4933-bc48-b4cd292cf501 | 17         | 480     | 6        | 2532        | True      |
-- | 521 | 2022-07-27 23:54:24 | a18c367c-9939-4414-bb1e-48afe8cdf565 | 74         | 480     | 3        | 1440        | True      |
-- | 873 | 2023-03-05 22:45:30 | 150ff85f-67d2-4e0b-a76c-f2450b2db6a3 | 6          | 480     | 1        | 403         | True      |
-- +-----+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------+

-- query orders which their created_at is greater than 2023-03-05 22:45:30
SELECT *
FROM orders
WHERE created_at > '2023-03-05 22:45:30';
-- +------+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------+
-- | id   | created_at          | order_code                           | product_id | user_id | quantity | total_price | delivered |
-- |------+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------|
-- | 2    | 2023-08-08 20:19:34 | c01b34e3-9db0-49ae-85b7-1efd16f0549d | 79         | 492     | 10       | 2370        | True      |
-- | 3    | 2023-08-15 05:16:22 | 4eefdca1-a8cb-446e-8b53-d3fe8f4c53b3 | 51         | 402     | 6        | 2064        | True      |
-- | 4    | 2023-09-11 19:20:27 | c16fa5cd-bd61-4771-9b52-fddc8adb8190 | 53         | 468     | 3        | 855         | True      |
-- | 5    | 2023-07-24 00:49:53 | fb6c3f59-eca6-4827-8d16-60d56bae3a5b | 145        | 276     | 5        | 2340        | True      |
-- | 6    | 2023-08-03 21:05:06 | c59628e4-9c10-44ef-a423-cd01edb73580 | 150        | 315     | 5        | 1345        | True      |
-- | 10   | 2023-07-28 03:23:57 | 42a8eff9-1c77-4527-9b5b-3eefba1da7f6 | 102        | 426     | 5        | 1565        | True      |
-- ...
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
