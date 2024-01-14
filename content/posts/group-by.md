---
title: "GROUP BY"
date: 2024-01-12T15:40:37+03:30
tags:
- query
- postgresql
---
`GROUP BY` comblines the output into groups of rows that matches on
one or multiple values. Also, `GROUP BY` usually used with aggregate functions
like `COUNT`, `MIN`, `MAX`, `SUM`, and `AVG`.
```sql
-- count number of products for each company
SELECT COUNT(id), company
FROM products
GROUP BY company;
-- +-------+---------------------------------+
-- | count | company                         |
-- |-------+---------------------------------|
-- | 1     | Edwards, Fox and Valentine      |
-- | 2     | Hale-Bryan                      |
-- | 1     | Alexander Inc                   |
-- | 1     | Stark and Sons                  |
-- | 2     | Martin, Baker and Henderson     |
-- ...

-- get number of orders of each user and order them
-- by the number of orders
SELECT COUNT(id), user_id
FROM orders
GROUP BY user_id
ORDER BY count desc;
-- +-------+---------+
-- | count | user_id |
-- |-------+---------|
-- | 8     | 332     |
-- | 7     | 367     |
-- | 7     | 456     |
-- | 6     | 192     |
-- | 6     | 307     |
-- | 6     | 194     |
-- ...
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
