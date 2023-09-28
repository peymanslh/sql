import sys

import psycopg

from data_generator import (
    gen_users, gen_product_categories,
    gen_products, gen_orders, gen_user_log,
    ListOfDicts,
)

# Change these numbers if you want more data
NUMBER_OF_PRODUCTS = 200
NUMBER_OF_USERS = 500
NUMBER_OF_ORDERS = 1100
NUMBER_OF_LOGS = 80000

def main():
    if len(sys.argv) < 2:
        raise Exception("Please pass database connection string")
    con_str = sys.argv[1]

    users = gen_users(NUMBER_OF_USERS)
    categories = gen_product_categories()
    products = gen_products(NUMBER_OF_PRODUCTS)
    orders = gen_orders(NUMBER_OF_ORDERS, users, products)
    logs = gen_user_log(NUMBER_OF_LOGS, users)

    create_tables(con_str)

    insert_to_sql(con_str, INSERT_USERS, users)
    insert_to_sql(con_str, INSERT_PRODUCT_CATEGORIES, categories)
    insert_to_sql(con_str, INSERT_PRODUCTS, products)
    insert_to_sql(con_str, INSERT_ORDERS, orders)
    insert_to_sql(con_str, INSERT_LOGS, logs)


def create_tables(con_str: str):
    query = ""
    with open("postgres_tables.sql", "r") as file:
        query = file.read()

    with psycopg.connect(con_str) as conn:
        with conn.cursor() as cur:
            cur.execute(query)


INSERT_USERS = """
INSERT INTO users
    (datetime_joined, first_name, last_name, email, city, active)
VALUES
    (%(datetime_joined)s, %(first_name)s, %(last_name)s, %(email)s, %(city)s, %(active)s);
"""

INSERT_PRODUCT_CATEGORIES = """
INSERT INTO product_categories
    (name)
VALUES
    (%(name)s);
"""

INSERT_PRODUCTS = """
INSERT INTO products
    (created_at, product_code, name, company, price, category_id, description)
VALUES
    (%(created_at)s, %(product_code)s, %(name)s, %(company)s, %(price)s, %(category_id)s, %(description)s);
"""

INSERT_ORDERS = """
INSERT INTO orders
    (created_at, order_code, product_id, user_id, quantity, total_price, delivered)
VALUES
    (%(created_at)s, %(order_code)s, %(product_id)s, %(user_id)s, %(quantity)s, %(total_price)s, %(delivered)s);
"""


INSERT_LOGS = """
INSERT INTO user_logs
    (user_email, datetime, ip_address, page_visited, user_agent)
VALUES
    (%(user_email)s, %(datetime)s, %(ip_address)s, %(page_visited)s, %(user_agent)s);
"""


def insert_to_sql(con_str: str, query: str, data: ListOfDicts):
    with psycopg.connect(con_str) as conn:
        with conn.cursor() as cur:
            cur.executemany(query, data)


if __name__ == "__main__":
  main()

