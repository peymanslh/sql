---
title: "Setup"
date: 2023-09-15T03:12:13+03:30
draft: false
---

If you want to run the examples in the following posts, you can 
follow these instructions to setup your environment and import 
our sample data to work with.

## PostgreSQL
If you have PostgreSQL installed, you can skip step 1 and 2.

### 1: Install docker and docker compose
You can download and install docker and docker compose from 
[docker website](https://www.docker.com/).  

### 2: Run PostgreSQL
Create a `docker-compose.yml` file:  
```yaml
version: '3'

services:
  postgres:
    image: postgres:latest
    environment:
      - POSTGRES_USER=sbe
      - POSTGRES_PASSWORD=sqlbyexample
      - POSTGRES_DB=sbe
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data/

volumes:
  postgres_data:
```
Then, run:
```bash
docker compose up -d
```

### 3: Import sample database
