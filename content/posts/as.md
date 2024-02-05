---
title: "AS"
date: 2024-02-05T11:01:38+03:30
tags:
- query
- postgresql
---
`AS` keyword is use to make an alias for a column name.
```sql
SELECT
  COUNT(id),
  AVG(total_price),
  user_id
FROM orders
GROUP BY user_id;
--     V      V
-- +-------+-----------------------+---------+
-- | count | avg                   | user_id |
-- |-------+-----------------------+---------|
-- | 1     | 2220.0000000000000000 | 384     |
-- | 3     | 1319.3333333333333333 | 351     |

-- Use alias for count and avg columns
SELECT
  COUNT(id) as number_of_orders,
  AVG(total_price) avg_total_price,
  user_id
FROM orders
GROUP BY user_id;
--          V                 V
-- +------------------+-----------------------+---------+
-- | number_of_orders | avg_total_price       | user_id |
-- |------------------+-----------------------+---------|
-- | 1                | 2220.0000000000000000 | 384     |
-- | 3                | 1319.3333333333333333 | 351     |
```
