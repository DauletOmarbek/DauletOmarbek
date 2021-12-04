create table products(
    UPC_code integer PRIMARY KEY,
    product_name varchar(20) NOT NULL,
    packaging varchar(20) NOT NULL CHECK (packaging in ('A', 'B', 'C')),
    size varchar(20) NOT NULL CHECK (size in ('1', '2', '3'))
);

create table price(
    UPC_code integer REFERENCES products(UPC_code),
    price integer CHECK (price > 0)
);

create table types(
    type_name varchar(50) PRIMARY KEY
);

create table product_types(
     UPC_code integer REFERENCES products(UPC_code),
    type_name varchar(50) REFERENCES types(type_name)
);

create table brands(
    brand_id integer PRIMARY KEY,
    brand_name varchar(20) NOT NULL
);

create table brand_product(
    UPC_code integer REFERENCES products(UPC_code),
    brand_id integer REFERENCES brands(brand_id)
);

create table vendors(
    vendors_id integer PRIMARY KEY,
    vendors_name varchar(50) NOT NULL
);

create table vendors_brands(
    vendors_id integer REFERENCES vendors(vendors_id),
    brand_id integer REFERENCES brands(brand_id)
);

create type namee as(
    first_name varchar(20),
    second_name varchar(20)
                   );

create type addresss as(
    country varchar(20),
    city varchar(20),
    street varchar(20)
                      );

create table stores(
    stores_id integer PRIMARY KEY,
    stores_name varchar(50) NOT NULL,
    extra_charge integer CHECK (0 < extra_charge),
    address addresss NOT NULL,
    start_time time NOT NULL,
    end_time time NOT NULL
);

create table stores_vendors(
    stores_id integer REFERENCES stores(stores_id),
    vendors_id integer REFERENCES vendors(vendors_id)
);

/*
create table price_stores(
    UPC_code integer REFERENCES products(UPC_code),
    stores_id integer REFERENCES stores(stores_id),
    price integer NOT NULL,
    extra_charge integer CHECK (0 < extra_charge),
    new_price integer GENERATED ALWAYS AS (price + price*extra_charge/100) STORED
);
*/

create table regular_customers(
    customer_id integer PRIMARY KEY,
    name namee NOT NULL,
    address addresss NOT NULL,
    phone_number varchar(14) NOT NULL,
    data_of_birth date NOT NULL
);

create table customer_orders(
    order_id serial PRIMARY KEY ,
    customers_id integer REFERENCES regular_customers(customer_id) ,
    store_id integer REFERENCES stores(stores_id),
    UPC_code integer NOT NULL,
    price integer NOT NULL CHECK(price > 0),
    time date NOT NULL
);

create table online_orders(
    online_order_id serial PRIMARY KEY,
    customers_id integer REFERENCES regular_customers(customer_id) ,
    store_id integer REFERENCES stores(stores_id),
    brands_id integer REFERENCES brands(brand_id),
    UPC_code integer NOT NULL,
    price integer NOT NULL CHECK(price > 0),
    time date NOT NULL
);

create table all_orders(
    order_id serial PRIMARY KEY,
    order_online bool,
    customers_id integer REFERENCES regular_customers(customer_id),
    store_id integer REFERENCES stores(stores_id),
    UPC_code integer REFERENCES products(UPC_code),
    price integer,
    time date NOT NULL
);

create or replace function alll_orders()
    returns TRIGGER
    LANGUAGE plpgsql
    as
    $$
    BEGIN
        insert into all_orders(order_online, customers_id, store_id, UPC_code, price, time)
        values (false,new.customers_id, new.store_id, new.UPC_code, new.price, new.time);
        return new;
    end;
    $$;

create or replace function allll_orders()
    returns TRIGGER
    LANGUAGE plpgsql
    as
    $$
    BEGIN
        insert into all_orders(order_online, customers_id, store_id, UPC_code, price, time)
        values (true,new.customers_id, new.store_id, new.UPC_code, new.price, new.time);
        return new;
    end;
    $$;

create TRIGGER insert_order
    BEFORE INSERT
    ON customer_orders
    FOR EACH ROW
    EXECUTE PROCEDURE alll_orders();

create TRIGGER insert_orderr
    BEFORE INSERT
    ON online_orders
    FOR EACH ROW
    EXECUTE PROCEDURE allll_orders();

