---
title: "IN"
date: 2024-02-09T15:17:05+03:30
tags:
- query
- postgresql
---
We can use `IN` to check a value against multiple other values.  
Or, we can think it as a shorthand for multiple `OR`.
```sql
-- get products with category of 1, 2, and 3
SELECT
  id,
  name,
  product_code,
  category_id
FROM products
WHERE category_id IN (1, 2, 3);
-- +-----+---------------+--------------+-------------+
-- | id  | name          | product_code | category_id |
-- |-----+---------------+--------------+-------------|
-- | 1   | teal paint    | 30248960     | 1           |
-- | 2   | olive paint   | 12996179     | 2           |
-- | 3   | olive paint   | 84201010     | 3           |
-- | 4   | silver paint  | 41798096     | 3           |
-- ...

-- find users with first_name if Ryan and Andrew
SELECT id, first_name, last_name FROM users WHERE first_name IN ('Ryan', 'Andrew');
-- +-----+------------+-----------+
-- | id  | first_name | last_name |
-- |-----+------------+-----------|
-- | 13  | Andrew     | Mercado   |
-- | 19  | Ryan       | Woods     |
-- | 38  | Ryan       | Beard     |
-- | 56  | Ryan       | Alexander |
-- | 84  | Andrew     | Castaneda |
-- ...
```
