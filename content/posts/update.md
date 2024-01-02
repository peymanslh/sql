---
title: "Update"
date: 2024-01-01T20:11:38+03:30
tags:
- modify
- postgresql
---
By choosing one or multiple columns and add a condition we can update
existing rows.

```sql
-- set active column of all rows in `users` table
-- when you don't provide a where condition with your update it will
-- update all rows in your table
-- Don't run this query on your sample database, until you know what you're doing
UPDATE
  users
SET
  active = true;

-- update first name and last name of a user based on his email
UPDATE
  users
SET
  first_name = 'Jamie',
  last_name = 'Smith'
WHERE
  email = 'davidowen@brown.com';

-- Update price of a product based on its current value
-- -add price by 10
UPDATE
  products
SET
  price = price + 10,
WHERE
  id = 45;
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-update.html)
