# This script genrates random data for an eCommerce website
#
# Requirements:
# - Faker==19.6.1
# - psycopg==3.1.10
#

import sys
from typing import Any
from datetime import datetime, timedelta

from faker import Faker
import psycopg

dtype = list[dict[str, Any]]

faker = Faker()

# Change these numbers if you want more data
NUMBER_OF_PRODUCTS = 100
NUMBER_OF_USERS = 150
NUMBER_OF_ORDERS = 500
NUMBER_OF_LOGS = 40000


def main():
    if len(sys.argv) < 2:
        raise Exception("Please pass database connection string")
    con_str = sys.argv[1]
    users = gen_users(NUMBER_OF_USERS)
    categories = gen_product_categories()
    products = gen_products(NUMBER_OF_PRODUCTS)
    orders = gen_orders(NUMBER_OF_ORDERS, users, products)
    logs = gen_user_log(NUMBER_OF_LOGS, users)

    insert_to_sql(con_str, users)
    from pprint import pp
    pp(logs)


def insert_to_sql(con_str: str, data: dtype):
    with psycopg.connect(con_str) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE test (
                    id serial PRIMARY KEY,
                    num integer,
                    data text)
                """)


def get_email(emails_list) -> str:
    while True:
        email = faker.ascii_email()
        if email not in emails_list:
            return email


def gen_users(count: int) -> dtype:
    result = []
    emails_list = []
    for i in range(1, count + 1):
        first_name = faker.first_name()
        last_name = faker.last_name()
        start_date = datetime.now() - timedelta(days=700)
        email = get_email(emails_list)
        emails_list.append(email)
        result.append({
            "id": i,
            "datetime_joined": faker.date_time_between(start_date=start_date),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "city": faker.city(),
            "active": faker.pybool(95),
        })
    return result


def gen_product_categories() -> dtype:
    paints = ["Oil Paint", "Alkyd Paint", "Spray Paint",]
    result = []
    for key, value in enumerate(paints):
        result.append({
            "id": key + 1,
            "name": value,
        })
    return result


def gen_companies(count: int) -> list[str]:
    result = []
    for _ in range(count):
        result.append(faker.company())
    return result


def get_product_code(codes_list) -> str:
    while True:
        code = faker.ean8()
        if code not in codes_list:
            return code


def gen_products(count: int) -> dtype:
    companies = gen_companies(count)
    categories = gen_product_categories()
    result = []
    codes_list = []
    for i in range(1, count + 1):
        start_date = datetime.now() - timedelta(days=700)
        code = get_product_code(codes_list)
        codes_list.append(code)
        result.append({
            "id": i,
            "created_at": faker.date_time_between(start_date=start_date),
            "product_code": code,
            "name": f"{faker.safe_color_name()} paint",
            "company": companies[faker.pyint(max_value=len(companies) - 1)],
            "price": faker.pyint(min_value=200, max_value=500),
            "category": categories[faker.pyint(max_value=len(categories) - 1)]["id"],
            "description": faker.text(max_nb_chars=100),
        })
    return result


def get_order_code(codes_list) -> str:
    while True:
        code = faker.uuid4()
        if code not in codes_list:
            return code


def gen_orders(count: int, users: dtype, products: dtype) -> dtype:
    result = []
    codes_list = []
    for i in range(1, count + 1):
        p = products[faker.pyint(max_value=len(products) - 1)]
        q = faker.pyint(min_value=1, max_value=10)
        u = users[faker.pyint(max_value=len(users) - 1)]
        code = get_order_code(codes_list)
        codes_list.append(code)
        result.append({
            "id": i,
            "created_at": faker.date_time_between(start_date=u["datetime_joined"]),
            "order_code": code,
            "product": p["id"],
            "user": u["id"],
            "quantity": q,
            "total_price": q * p["price"],
            "delivered": faker.pybool(95),
        })
    return result


def gen_user_log(count: int, users: dtype) -> dtype:
    result = []
    for i in range(1, count + 1):
        u = users[faker.pyint(max_value=len(users) - 1)]
        result.append({
            "id": i,
            "user_email": u["email"],
            "datetime": faker.date_time_between(start_date=u["datetime_joined"]),
            "ip_address": faker.ipv4_public(),
            "page_visited": faker.uri_path(),
            "user_agent": faker.user_agent(),
        })
    return result


if __name__ == "__main__":
  main()

