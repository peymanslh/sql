---
title: "Create and Drop Table"
date: 2023-09-17T01:06:01+03:30
tags:
- manage
- postgresql
---
### Create table
By using `CREATE TABLE` statement you can create a new table.
```sql
-- Create a table called users
CREATE TABLE users (
  id SERIAL PRIMARY KEY, -- auto increment primary key, handles 1 to 2,147,483,647
  -- Or use BIGSERIAL that handles from up to 9,223,372,036,854,775,807
  first_name VARCHAR NOT NULL, -- varchar column that can't be null
  last_name VARCHAR (255),
  created_at TIMESTAMP, -- without time zone,
  updated_at TIMESTAMP WITH TIME ZONE, -- or use timestamptz
  code INTEGER,
  rate double precision, -- double precision floating-point number
  active BOOLEAN DEFAULT true, -- boolean with default value of true
  group_id INTEGER NOT NULL,
  -- PRIMARY KEY (col1, col2), make col1 and col2 as primary key
  FOREIGN KEY (group_id)
      REFERENCES groups (group_id) -- set foreign key on another table
);
```
[PostgreSQL docs - create table](https://www.postgresql.org/docs/16/sql-createtableas.html)  
[PostgreSQL docs - data types](https://www.postgresql.org/docs/8.1/datatype.html#DATATYPE-TABLE)  

## Remove table
Use `DROP TABLE` to destroy a table.
```sql
-- drop table coffee
DROP TABLE coffee;

-- Doesn't throw error when table doesn't exists
DROP TABLE IF EXISTS coffee;

-- Also drop objects that depend on this table like views
DROP TABLE coffee CASCADE;
```
[PostgreSQL docs](https://www.postgresql.org/docs/16/sql-droptable.html)  
