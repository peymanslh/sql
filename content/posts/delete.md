---
title: "Delete"
date: 2024-01-01T20:40:45+03:30
---
With `DELETE` we can delete one or multiple rows from a table.

{{< tabs tabTotal="1" >}}
{{< tab tabName="PostgreSQL" >}}
```sql
-- when you don't provide a where condition with your delete it will
-- delete all rows in your table
-- Don't run this query on your sample database, until you know what you're doing
DELETE FROM orders;

-- delete all orders of a user with id of 10
DELETE FROM
  orders
WHERE
  user_id = 12;
```

Read more about Delete on 
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-delete.html)

{{< /tab >}}
{{< /tabs >}}
