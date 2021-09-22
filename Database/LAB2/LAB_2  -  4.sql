--1
create  table customers(
    id integer PRIMARY KEY ,
    full_name varchar(50) NOT NULL,
    timestamp timestamp NOT NULL,
    delivery_address text NOT NULL
)

insert into customers (id, full_name, timestamp,delivery_address) values  ('123', 'Daulet','2015-12-31', 'M.Mahmutov');

update customers
set delivery_address = 'Almaty'
where full_name = 'Daulet'

delete
from  customers
where full_name = 'Omarbek'


--2
create table orders(
    code integer PRIMARY KEY ,
    customer_id integer REFERENCES customers(id),
    total_sum double precision NOT NULL CHECK ( total_sum > 0 ),
    is_paid boolean NOT NULL
)

insert into orders (code, customer_id, total_sum, is_paid) values  ('12345678', '123', '50000', '1500');

update orders
set total_sum = total_sum + 50000
where code = '12354678'

delete
from  orders
where is_paid = '10000'

--3
create table products(
    id varchar PRIMARY KEY ,
    name varchar NOT NULL ,
    description text NOT NULL ,
    price double precision NOT NULL CHECK ( price > 0 )
)

insert into products (id, name, description, price) values  ('123', 'Daulet','Red', '500000' );

update products
set price = price + 50000
where name = 'table'

delete
from  products
where name = 'table'

--4
create table order_items(
    order_code integer REFERENCES orders (code),
    product_id varchar REFERENCES products (id),
    quantity integer NOT NULL CHECK ( quantity > 0 )
)

insert into order_items ( order_code, product_id, quantity ) values  ('12345678', '123', '30');

update order_items
set quantity = order_items.quantity + 10
where order_code = '12345678'

delete
from  order_items
where order_code = '12345678'
