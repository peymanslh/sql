---
title: "Create and Drop Database"
date: 2023-09-17T00:50:10+03:30
---

## PostgreSQL
### Create Database
With `CREATE DATABASE` statement you can create a new database in PostgreSQL.
```sql
-- create a database called coffee
CREATE DATABASE coffee; 
```
You can see more options to create a database in 
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-createdatabase.html)

### Remove database
Use `DROP DATABASE` statement to remove a database.
```sql
-- drop a database called coffe
DROP DATABASE coffee;

-- Force to drop the database if anyone is connected to it
DROP DATABASE coffee FORCE;

-- Doesn't thorw an error if database doesn't exist
DROP DATABASE IF EXISTS coffee;
```
[Drop database in PostgreSQL docs](https://www.postgresql.org/docs/current/sql-dropdatabase.html)

