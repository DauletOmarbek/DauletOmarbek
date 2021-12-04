create table stores(
    extra_charge integer CHECK (0 < extra_charge),
    price integer NOT NULL,
    new_price integer GENERATED ALWAYS AS (price + price*extra_charge/100) STORED,
    start_time time NOT NULL,
    end_time time NOT NULL
)

insert into stores(extra_charge, price,start_time,end_time) values (10, 150,'10:00:00','22:00:00' )

create table regular_customers(
    fisrt_name varchar(20) NOT NULL,
    second_name varchar(20) NOT NULL,
    country varchar(20) NOT NULL,
    city varchar(20),
    street varchar(20),
    phone_number varchar(14) NOT NULL,
    data_of_birth date NOT NULL
);

insert into regular_customers values (1,ROW('Daulet','Omarbek'),ROW('Kazashtan','Kyzylorda','Mahmutov'),'87773848464','2002-12-04')

insert into regular_customers values (1,ROW('Aidana','Omarbek'),ROW('Kazashtan','Kyzylorda','Mahmutov'),'87773848464','2002-12-04')