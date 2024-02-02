---
title: "AND, OR, NOT"
date: 2024-02-02T14:18:01+03:30
tags:
- query
- postgresql
---
With the help of `AND`, `OR`, and `NOT` we can add more power to
our query conditions.
```sql
-- select all orders with product_id of 10 and delivered
-- only select rows where both conditions are true
SELECT *
FROM orders
WHERE
  product_id = '10' AND
  delivered = true;
-- +-----+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------+
-- | id  | created_at          | order_code                           | product_id | user_id | quantity | total_price | delivered |
-- |-----+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------|
-- | 113 | 2023-07-08 21:09:44 | 12f82968-46fc-4118-9c58-fb568c38fa4e | 10         | 343     | 1        | 445         | True      |
-- | 121 | 2023-06-03 00:18:42 | 24d070f9-2e4b-4b41-8d76-c99167083405 | 10         | 239     | 8        | 3560        | True      |
-- | 487 | 2023-07-04 06:34:56 | 23da1388-e818-48af-ab5b-bc14951a22e0 | 10         | 41      | 5        | 2225        | True      |
-- | 774 | 2023-04-20 09:35:38 | 07bbf026-ef4f-4078-a919-48702af47cb0 | 10         | 67      | 3        | 1335        | True      |
-- +-----+---------------------+--------------------------------------+------------+---------+----------+-------------+-----------+

-- select all users where their first or last name is John
-- select rows where only one of the conditions are true
SELECT *
FROM users
WHERE first_name = 'John' OR
last_name = 'John';
-- +-----+---------------------+------------+-----------+------------------------------+-----------------+--------+
-- | id  | datetime_joined     | first_name | last_name | email                        | city            | active |
-- |-----+---------------------+------------+-----------+------------------------------+-----------------+--------|
-- | 14  | 2022-12-18 03:47:51 | John       | Combs     | katherinewiley@myers.com     | Port Anthony    | True   |
-- | 51  | 2022-07-05 12:04:27 | John       | Fritz     | darren27@gmail.com           | Masonborough    | True   |
-- | 285 | 2021-11-17 01:40:06 | John       | Sanders   | ygordon@yahoo.com            | Erinfurt        | True   |
-- ...

-- select all products without the ones that their company
-- name is 'Allen-Jones'
SELECT
  created_at,
  product_code,
  name,
  company,
  price
FROM products
WHERE NOT company = 'Allen-Jones';
-- +---------------------+--------------+---------------+---------------------------------+-------+
-- | created_at          | product_code | name          | company                         | price |
-- |---------------------+--------------+---------------+---------------------------------+-------|
-- | 2023-09-01 23:59:14 | 30248960     | teal paint    | Burke, Payne and Oliver         | 427   |
-- | 2022-09-09 15:49:58 | 12996179     | olive paint   | Alexander Inc                   | 377   |
-- | 2022-01-07 00:53:59 | 84201010     | olive paint   | Gray, Carson and Oneill         | 402   |
-- ...
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
