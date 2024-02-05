---
title: "MIN, MAX"
date: 2024-02-03T15:49:57+03:30
tags:
- query
- postgresql
- aggregate
- functions
---
`MIN` returns the smallest value of a column.
`MAX` returns the biggest value of a column.
```sql
-- return the lowest total_price from orders of user with id of 10
SELECT MIN(total_price) FROM orders WHERE user_id = 10;
-- +------+
-- | min  |
-- |------|
-- | 1132 |
-- +------+

-- return the highest total_price from the orders of user with id of 10
SELECT MAX(total_price) FROM orders WHERE user_id = 10;
-- +------+
-- | max  |
-- |------|
-- | 1998 |
-- +------+
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/tutorial-agg.html)

