---
title: "LIMIT"
date: 2024-02-02T15:09:44+03:30
tags:
- query
- postgresql
---
When the number of rows in a select query are a lot, we can limit
them by the `LIMIT` statement.
```sql
-- only return 3 item
SELECT * FROM users LIMIT 3;
-- +----+---------------------+------------+-----------+--------------------------------+----------------+--------+
-- | id | datetime_joined     | first_name | last_name | email                          | city           | active |
-- |----+---------------------+------------+-----------+--------------------------------+----------------+--------|
-- | 1  | 2023-08-18 21:44:13 | Carmen     | Malone    | rmcconnell@yahoo.com           | East Jeanmouth | True   |
-- | 2  | 2023-07-27 04:31:11 | Stephanie  | Wallace   | hjennings@curry.com            | West Misty     | True   |
-- | 3  | 2023-01-30 08:00:52 | Brandon    | Jenkins   | lrichardson@meadows-hodges.biz | Pinedamouth    | True   |
-- +----+---------------------+------------+-----------+--------------------------------+----------------+--------+
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
