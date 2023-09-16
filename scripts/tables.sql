
CREATE TABLE users (
  id serial PRIMARY KEY,
  datetime_joined TIMESTAMP NOT NULL,
  first_name VARCHAR,
  last_name VARCHAR,
  email VARCHAR NOT NULL,
  city VARCHAR,
  active BOOLEAN
);

CREATE TABLE product_categories (
  id serial PRIMARY KEY,
  name VARCHAR NOT NULL
);

CREATE TABLE products (
  id serial PRIMARY KEY,
  created_at TIMESTAMP,
  product_code VARCHAR NOT NULL,
  name VARCHAR NOT NULL,
  company VARCHAR,
  price INT,
  category INT NOT NULL,
  description TEXT,

  FOREIGN KEY (category) REFERENCES product_categories (id)
);

CREATE TABLE orders (
  id serial PRIMARY KEY,
  created_at TIMESTAMP,
  order_code VARCHAR NOT NULL,
  product INT NOT NULL,
  user INT NOT NULL,
  quantity INT,
  total_price INT,
  delivered BOOLEAN,

  FOREIGN KEY (product) REFERENCES products (id),
  FOREIGN KEY (user) REFERENCES users (id)
);

CREATE TABLE user_logs (
  id serial PRIMARY KEY,
  user_email VARCHAR NOT NULL,
  datetime TIMESTAMP,
  ip_address VARCHAR,
  page_visited TEXT,
  user_agent TEXT
);
