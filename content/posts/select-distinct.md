---
title: "SELECT DISTINCT"
date: 2024-02-09T14:25:06+03:30
tags:
- query
- postgresql
---
The `SELECT DISTINCT` statement returns the distinct (different) values of a column.  
Unlike `SELECT` that returns all values of a column.  
You can run the bellow queries and compare the result.  
```sql
-- return distinct of company names(which is unique values)
SELECT DISTINCT company
FROM products
ORDER BY company;
-- +---------------------------------+
-- | company                         |
-- |---------------------------------|
-- | Adkins, Short and Maxwell       |
-- | Alexander Inc                   |
-- | Allen-Jones                     |
-- | Anderson-Santiago               |
-- | Andrews Group                   |
-- | Austin, Brown and Marshall      |
-- | Baker and Sons                  |
-- ...

-- without distinct, which retuns company names with duplicate values
SELECT company
FROM products
ORDER BY company;
-- +---------------------------------+
-- | company                         |
-- |---------------------------------|
-- | Adkins, Short and Maxwell       |
-- | Adkins, Short and Maxwell       |
-- | Alexander Inc                   |
-- | Allen-Jones                     |
-- | Allen-Jones                     |
-- | Anderson-Santiago               |
-- | Andrews Group                   |
-- | Andrews Group                   |
-- ...

-- use count and get the number of companies
SELECT COUNT(DISTINCT company) FROM products;
-- +-------+
-- | count |
-- |-------|
-- | 122   |
-- +-------+
```
[PostgreSQL docs](https://www.postgresql.org/docs/current/sql-select.html)
