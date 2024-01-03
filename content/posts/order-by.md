---
title: "ORDER BY"
date: 2024-01-03T23:55:35+03:30
tags:
- query
- postgresql
---
In a select query, after choosing the columns and adding some conditions
we can choose the ordering of the output data based on a columns which
can be an integer, datetime or some other kinds of sortable data types.  
By adding `ORDER BY` we can sort the output.

```sql
-- list orders and sort them by total_price
-- this will list them from lowest to highest
SELECT
  id, order_code, quantity, total_price
FROM orders
ORDER BY total_price;
-- +------+--------------------------------------+----------+-------------+
-- | id   | order_code                           | quantity | total_price |
-- |------+--------------------------------------+----------+-------------|
-- | 917  | 27fdbd2b-1fa0-4633-ac2f-1f007fd9d6e2 | 1        | 200         |
-- | 266  | 95b02f2a-bedd-4ad5-b767-3854cb886ef9 | 1        | 201         |
-- | 871  | e232f447-4bae-4c45-b4d2-87663217df0a | 1        | 206         |
-- | 89   | b2c93d87-0169-4152-986e-ee3fa20ff50c | 1        | 210         |
-- | 200  | a7a612cd-6f1d-4844-b19c-d588530863fb | 1        | 211         |
-- ... 

-- also, we can add ASC for ascending and DESC for descending
-- this will list them from highest to lowest
SELECT
  id, order_code, quantity, total_price
FROM orders
ORDER BY total_price DESC;
-- +------+--------------------------------------+----------+-------------+
-- | id   | order_code                           | quantity | total_price |
-- |------+--------------------------------------+----------+-------------|
-- | 85   | fc39120d-4f60-4247-afd8-3cbb54756615 | 10       | 5000        |
-- | 748  | 98f6f01b-30f5-4bdb-ba24-907429a87723 | 10       | 5000        |
-- | 522  | 082cea22-1879-461b-8143-3e3f4bca8ec1 | 10       | 4900        |
-- | 655  | 1e0d5ccf-2de0-4ab5-a7d9-e1d5254df279 | 10       | 4800        |
-- | 562  | f27b585f-f180-4468-9249-02aa04631275 | 10       | 4800        |
-- | 533  | 4ac59eda-cbe1-4cd2-b3da-9ed930e87646 | 10       | 4750        |
-- ...

-- we can sort the output by two columns
-- this query will sort the users by their first_name, and if their 
-- first_name is equal then, sort them by their last_name
SELECT
  id, first_name, last_name
FROM users
ORDER BY
  first_name ASC,
  last_name ASC;
-- +-----+-------------+-------------+
-- | id  | first_name  | last_name   |
-- |-----+-------------+-------------|
-- | 205 | Adam        | Gilmore     |
-- | 42  | Adrian      | Ewing       |
-- | 182 | Albert      | Farley      |
-- | 419 | Alexander   | Brown       |
-- | 157 | Alexander   | Gonzalez    |
-- | 186 | Alicia      | Garrett     |
-- | 188 | Amanda      | Johnson     |
-- | 371 | Amanda      | Kane        |
-- | 450 | Amanda      | Myers       |
-- | 460 | Amanda      | Olson       |
-- | 461 | Amanda      | Robinson    |
-- ...
```

[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
