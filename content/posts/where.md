---
title: "Where"
date: 2023-12-30T23:17:01+03:30
tags:
- query
- postgresql
---
With `WHERE` we can add a condition to our queries.
```sql
-- query user with email of rmcconnell@yahoo.com
SELECT
  first_name, last_name, email
FROM users
WHERE email = 'rmcconnell@yahoo.com';

-- query orders by a user with id of 480
SELECT *
FROM orders
WHERE user_id = 480;

-- query orders by created_at
SELECT *
FROM orders
WHERE created_at > '2023-03-05 22:45:30';
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
