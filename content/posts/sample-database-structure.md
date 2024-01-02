---
title: "Sample Database Structure"
date: 2023-09-15T16:23:58+03:30
tags:
- intro
- postgresql
---

This is an overview of sample database that you imported from [setup](/posts/setup/) post.

## Overview
We're assuming that we have an eCommerce website and have some tables 
like, users, product_categories, products, orders, and user_logs.

### Users table
Users table have the following structure.  
table name: users
|column |type |
|---|---|
id |int
datetime_joined |datetime
first_name |varchar
last_name |varchar
email |varchar
city |varchar
active |boolean

Sample data:  
|id |datetime_joined |first_name |last_name |email |city |active |
|---|---|---|---|---|---|---|
|1 |2023-03-07 12:45:12.231069+00 |John|Doe |john@sbe.com |West Misty | true


### Product categories
table name: product_categories
|column |type |
|---|---|
id |int
name |varchar

Sample data:  
|id |name |
|---|---|
|1 |Oil Paint 


### Products table
table name: products
|column |type |
|---|---|
id |int
created_at |datetime
product_code |varchar
name |varchar
company |varchar
price |int
category_id |int - foreign key
description |text

Sample data:  
|id |created_at |product_code |name |company |price |category_id |description |
|---|---|---|---|---|---|---|---|
|1 |2023-09-01 23:59:14 |30248960 |teal paint |Burke, Payne and Oliver |427 |1 |Score finally...


### Orders table
table name: orders
|column |type |
|---|---|
id |int
created_at |datetime
order_code |varchar
product_id |int - foreign key
user_id |int - foreign key
quantity |int
total_price |int
delivered |boolean

Sample data:  
|id |created_at |order_code |product_id |user_id |quantity |total_price |delivered |
|---|---|---|---|---|---|---|---|
|1 |2022-10-08 17:50:42 |28e9fe61-8883-4933-bc48-b4cd292cf501 |17 |480 |6 |2532 |True


### User logs table
table name: user_logs
|column |type |
|---|---|
id |int
user_email |varchar
datetime |datetime
ip_address |varchar
page_visited |text
user_agent |text

Sample data:  
|id |user_email |datetime |ip_address |page_visited |user_agent |
|---|---|---|---|---|---|
|1 |marilyn05@hotmail.com |2023-06-25 11:04:28 |116.0.78.131 |blog/ |Mozilla/5.0 (Windows; U; Windows CE)...
