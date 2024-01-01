---
title: "Insert"
date: 2024-01-01T19:43:54+03:30
---
We can insert new rows into our tables by using `INSERT` statement.

{{< tabs tabTotal="1" >}}
{{< tab tabName="PostgreSQL" >}}
```sql
-- insert new row(user) into users table
INSERT INTO
  users(datetime_joined, first_name, last_name, email, city, active)
VALUES
  ('2024-01-01 20:20:33', 'John', 'Moreno', 'sampleemil@email.com', 'Berlin', true);

-- insert multiple rows
INSERT INTO
  users(datetime_joined, first_name, last_name, email, city, active)
VALUES
  ('2024-01-01 20:20:33', 'John', 'Moreno', 'sampleemil@email.com', 'Berlin', true),
  ('2024-01-01 20:20:33', 'Brent', 'Cox', 'brentemail@email.com', 'Amsterdam', true);

-- by puting `RETURNING *` at the end of insert statement 
-- it returns inserted row back to you or show you in the console
INSERT INTO
  users(datetime_joined, first_name, last_name, email, city, active)
VALUES
  ('2024-01-01 20:20:33', 'John', 'Moreno', 'sampleemil2@email.com', 'Berlin', true)
RETURNING *;
```

Read more about Insert on 
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-insert.html)

{{< /tab >}}
{{< /tabs >}}
