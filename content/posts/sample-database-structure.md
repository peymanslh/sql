---
title: "Sample Database Structure"
date: 2023-09-15T16:23:58+03:30
draft: false
---

This is an overview of sample database that you imported from [setup]() post.

## Overview
We're assuming that we have an eCommerce website and have some tables 
like, users, products, orders, and users_log.

### Users table
Users table have the following structure.  

|column |type |
|---|---|
id |int
datetime_joined |datetime
first_name |varchar
last_name |varchar
email |varchar
username |varchar
active |boolean

Sample data:  
|id |datetime_joined |first_name |last_name |email |username |active |
|---|---|---|---|---|---|---|
|1 |2023-03-07 12:45:12.231069+00 |John|Doe |john@sbe.com |john_doe | true


### Products table
Products table have the following structure.  

|column |type |
|---|---|
id |int
created_at |datetime
name |varchar
price |int
category |foreign key
description |varchar
sale_price |int / nullable

Sample data:  
|id |datetime_joined |first_name |last_name |email |username |active |
|---|---|---|---|---|---|---|
|1 |2023-03-07 12:45:12.231069+00 |John|Doe |john@sbe.com |john_doe | true


