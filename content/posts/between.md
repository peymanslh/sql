---
title: "BETWEEN"
date: 2024-02-09T16:50:38+03:30
tags:
- query
- postgresql
---
`BETWEEN` is use to check if a value is greater and less than two other values.
```sql
-- get all orders between two dates
SELECT
  id,
  created_at,
  order_code
FROM orders
WHERE
  created_at BETWEEN '2023-06-17 15:38:12' AND '2023-07-17 15:38:12';
-- +------+---------------------+--------------------------------------+
-- | id   | created_at          | order_code                           |
-- |------+---------------------+--------------------------------------|
-- | 13   | 2023-07-08 21:50:22 | cbb06fd6-8060-483e-9e74-a0a3342cdbcd |
-- | 19   | 2023-06-17 15:38:12 | eb5b7b14-87ca-4cc5-8d83-3b929bc46b24 |
-- | 34   | 2023-07-03 13:39:39 | 36003e18-08bb-49ca-8dc4-ebb7ea96e9dd |
-- | 36   | 2023-07-14 21:38:56 | 31c0ec36-ce5f-4892-96e6-90593d2f50c6 |
-- ...

-- get all orders that their quantity is between 3 and 5
SELECT
  id,
  created_at,
  order_code,
  quantity
FROM orders
WHERE quantity BETWEEN 3 AND 5;
-- +------+---------------------+--------------------------------------+----------+
-- | id   | created_at          | order_code                           | quantity |
-- |------+---------------------+--------------------------------------+----------|
-- | 4    | 2023-09-11 19:20:27 | c16fa5cd-bd61-4771-9b52-fddc8adb8190 | 3        |
-- | 5    | 2023-07-24 00:49:53 | fb6c3f59-eca6-4827-8d16-60d56bae3a5b | 5        |
-- | 6    | 2023-08-03 21:05:06 | c59628e4-9c10-44ef-a423-cd01edb73580 | 5        |
-- | 9    | 2022-11-05 19:07:36 | 3a86364b-1d65-4514-9926-f8efb75752b3 | 3        |
-- | 10   | 2023-07-28 03:23:57 | 42a8eff9-1c77-4527-9b5b-3eefba1da7f6 | 5        |
-- | 12   | 2022-12-16 11:03:44 | 1b873d80-31d0-4820-b458-d85de2b4e369 | 5        |
-- | 13   | 2023-07-08 21:50:22 | cbb06fd6-8060-483e-9e74-a0a3342cdbcd | 5        |
-- | 16   | 2022-10-07 16:53:04 | c2fbf440-9375-4a03-8b05-e9bff77867ea | 4        |
-- ...
```
