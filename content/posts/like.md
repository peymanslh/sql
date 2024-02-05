---
title: "LIKE"
date: 2024-02-05T11:17:10+03:30
tags:
- query
- postgresql
---
`LIKE` is use in `WHERE` condition to find data based on a pattern.  
There are two wildcards that we can use with `LIKE`:  
- `%`: represents zero, one, or multiple characters
- `_`: represents one, single character.
```sql
-- find all users with first_name of John
SELECT
  id,
  first_name,
  last_name
FROM users
WHERE first_name LIKE 'John';
-- +-----+------------+-----------+
-- | id  | first_name | last_name |
-- |-----+------------+-----------|
-- | 14  | John       | Combs     |
-- | 51  | John       | Fritz     |
-- | 285 | John       | Sanders   |
-- | 445 | John       | Wise      |
-- | 485 | John       | Peterson  |
-- | 501 | John       | Moreno    |
-- | 502 | John       | Moreno    |
-- +-----+------------+-----------+

-- find all users that their first_name starts with A
SELECT
  id,
  first_name,
  last_name
FROM users
WHERE first_name LIKE 'A%';
-- +-----+------------+-----------+
-- | id  | first_name | last_name |
-- |-----+------------+-----------|
-- | 13  | Andrew     | Mercado   |
-- | 42  | Adrian     | Ewing     |
-- | 74  | Audrey     | Edwards   |

-- find all users that their first_name ends with n
SELECT
  id,
  first_name,
  last_name
FROM users
WHERE first_name LIKE '%n';
-- +-----+------------+-----------+
-- | id  | first_name | last_name |
-- |-----+------------+-----------|
-- | 1   | Carmen     | Malone    |
-- | 3   | Brandon    | Jenkins   |
-- | 7   | Jocelyn    | Williams  |
-- | 10  | Steven     | Perez     |
-- ...

-- find all users that their first_name contains n
SELECT
  id,
  first_name,
  last_name
FROM users
WHERE first_name LIKE '%n%';
-- +-----+------------+-----------+
-- | id  | first_name | last_name |
-- |-----+------------+-----------|
-- | 1   | Carmen     | Malone    |
-- | 2   | Stephanie  | Wallace   |
-- | 3   | Brandon    | Jenkins   |
-- | 5   | Jennifer   | Smith     |
-- ...

-- find all users that their first_name is 4 character and ends with arl
SELECT
  id,
  first_name,
  last_name
FROM users
WHERE first_name LIKE '_arl';
-- +-----+------------+------------+
-- | id  | first_name | last_name  |
-- |-----+------------+------------|
-- | 59  | Earl       | Livingston |
-- | 210 | Carl       | Gonzalez   |
-- | 382 | Karl       | Pierce     |
-- | 412 | Earl       | Owens      |
-- +-----+------------+------------+
```
[PostgreSQL docs](https://www.postgresql.org/docs/16/functions-matching.html#FUNCTIONS-LIKE)
