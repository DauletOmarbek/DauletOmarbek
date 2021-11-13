create table customers (
    id integer primary key,
    name varchar(255) NOT NULL,
    birth_date date NOT NULL
);

create table accounts(
    account_id varchar(40) primary key ,
    customer_id integer references customers(id),
    currency varchar(3) NOT NULL ,
    balance float NOT NULL default 0,
    "limit" float NOT NULL default 0
);

create table transactions (
    id serial primary key ,
    date timestamp NOT NULL,
    src_account varchar(40) references accounts(account_id),
    dst_account varchar(40) references accounts(account_id),
    amount float NOT NULL,
    status varchar(20) NOT NULL
);

DROP table transactions
DROP table accounts
DROP table customers