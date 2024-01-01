---
title: "Select"
date: 2023-12-26T23:41:25+03:30
---

By using `SELECT` statement we can reterive data from database.
Here is some examples of fetching data with `SELECT`.

{{< tabs tabTotal="1" >}}
{{< tab tabName="PostgreSQL" >}}
Select first_name, last_name and email columns from users table
```sql
SELECT first_name, last_name, email FROM users;
```
Output:
```
+-------------+-------------+---------------------------------------+
| first_name  | last_name   | email                                 |
|-------------+-------------+---------------------------------------|
| Carmen      | Malone      | rmcconnell@yahoo.com                  |
| Stephanie   | Wallace     | hjennings@curry.com                   |
| Brandon     | Jenkins     | lrichardson@meadows-hodges.biz        |
...
```
Select all columns from users table

```sql
SELECT * FROM users;
```
Output:
```
+-----+---------------------+-------------+-------------+---------------------------------------+-------------------------+--------+
| id  | datetime_joined     | first_name  | last_name   | email                                 | city                    | active |
|-----+---------------------+-------------+-------------+---------------------------------------+-------------------------+--------|
| 1   | 2023-08-18 21:44:13 | Carmen      | Malone      | rmcconnell@yahoo.com                  | East Jeanmouth          | True   |
| 2   | 2023-07-27 04:31:11 | Stephanie   | Wallace     | hjennings@curry.com                   | West Misty              | True   |
| 3   | 2023-01-30 08:00:52 | Brandon     | Jenkins     | lrichardson@meadows-hodges.biz        | Pinedamouth             | True   |
...
```

Read more about Select on 
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)

{{< /tab >}}
{{< /tabs >}}
