--1)How can we store large-object types?
-Usually large objects are stored outside the database
--2
--a
create role accountant;
grant all privileges on accounts to accountant;

create role administrator;
grant all privileges on customers,transactions,accounts to administrator;

create role support;
grant select on customers, transactions, accounts to support;

--b
create user Rahat;
grant accountant to Rahat;

create user Daulet;
grant administrator to Daulet;

create user Magzhan;
grant support to Magzhan;

--c
grant Magzhan to Daulet;

--d
revoke delete on accounts from accountant;



--5
--a
create unique index customer_index on accounts(account_id, currency)

--b
create index index_transactions on accounts(currency, balance)

--6
begin;
    update accounts set balance = balance - 150 where account_id = 'AB10203';
    update accounts set balance = balance + 150 where account_id = 'NK90123';
    rollback;
commit;