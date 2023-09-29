---
title: "Setup"
date: 2023-09-15T03:12:13+03:30
draft: false
---

If you want to run the examples in the following posts, you can 
follow these instructions to setup your environment and import 
our sample data to work with.

{{< tabs tabTotal="1" >}}
{{< tab tabName="PostgreSQL" >}}
If you have PostgreSQL installed, you can skip step 1.

### 1: Run PostgreSQL
You can download and install docker and docker compose from 
[docker website](https://www.docker.com/).  
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
# or
docker-compose up -d
```

### 2: Import data
Run this command to import backup into your PostgreSQL database.
```bash
# download backup file
wget https://raw.githubusercontent.com/peymanslh/sql/main/scripts/backups/sbe.pgsql

# import data
cat sbe.pgsql | docker exec -i `docker ps -q --filter name=postgres` psql -U sbe sbe
# or, if you don't use docker
psql -U sbe sbe < sbe.pgsql
```
You can download `sbe.pgsql` backup file from [GitHub](https://github.com/peymanslh/sql/tree/main/scripts/backups) 
or generate more data with scripts we provided in [`scripts` directory](https://github.com/peymanslh/sql/tree/main/scripts).  
{{< /tab >}}
{{< /tabs >}}
