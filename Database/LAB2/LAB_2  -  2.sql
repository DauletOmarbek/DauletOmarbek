create  table customers(
    id integer PRIMARY KEY ,
    full_name varchar(50) NOT NULL,
    timestamp timestamp NOT NULL,
    delivery_address text NOT NULL
)


create table orders(
    code integer PRIMARY KEY ,
    customer_id integer REFERENCES customers(id),
    total_sum double precision NOT NULL CHECK ( total_sum > 0 ),
    is_paid boolean NOT NULL
)


create table products(
    id varchar PRIMARY KEY ,
    name varchar NOT NULL ,
    description text NOT NULL ,
    price double precision NOT NULL CHECK ( price > 0 )
)

create table order_items(
    order_code integer REFERENCES orders (code),
    product_id varchar REFERENCES products (id),
    quantity integer NOT NULL CHECK ( quantity > 0 )
)

