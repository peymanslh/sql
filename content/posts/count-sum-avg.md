---
title: "COUNT, SUM, AVG"
date: 2024-02-04T13:45:07+03:30
tags:
- query
- postgresql
- aggregate
- functions
---
`COUNT` returns the number of rows for a column.
```sql
-- return the number of all users
SELECT COUNT(*) FROM users;
-- +-------+
-- | count |
-- |-------|
-- | 502   |
-- +-------+

-- find the number of orders by each user
SELECT
  COUNT(*),
  user_id
FROM orders
GROUP BY user_id
ORDER BY user_id;
-- +-------+---------+
-- | count | user_id |
-- |-------+---------|
-- | 2     | 1       |
-- | 1     | 2       |
-- | 3     | 3       |
-- | 4     | 4       |
-- ...
```

`SUM` returns the sum of a numeric column.
```sql
-- returns the sum of all of our orders
SELECT SUM(total_price) FROM orders;
-- +---------+
-- | sum     |
-- |---------|
-- | 2095239 |
-- +---------+

-- get the number of orders and average total price of them for user with id of 10
SELECT
  COUNT(id),
  AVG(total_price)
FROM orders
WHERE user_id = 10;
-- +-------+-----------------------+
-- | count | avg                   |
-- |-------+-----------------------|
-- | 4     | 1771.0000000000000000 |
-- +-------+-----------------------+
```


`AVG` returns the average of a numeric column.
```sql
-- returns the average total_price of all of our orders
SELECT AVG(total_price) FROM orders;
-- +-----------------------+
-- | avg                   |
-- |-----------------------|
-- | 1904.7627272727272727 |
-- +-----------------------+

-- get the number of orders and sum of total price of them for user with id of 10
SELECT
  COUNT(id),
  SUM(total_price)
FROM orders
WHERE user_id = 10;
-- +-------+------+
-- | count | sum  |
-- |-------+------|
-- | 4     | 7084 |
-- +-------+------+
```

[PostgreSQL docs](https://www.postgresql.org/docs/current/tutorial-agg.html)
