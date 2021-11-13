--1
create role accountant;
grant all privileges on accounts to accountant;

create role administrator;
grant all privileges on customers,transactions,accounts to administrator;

create role support;
grant select on customers, transactions, accounts to support;

--2
create user Rahat;
grant accountant to Rahat;

create user Daulet;
grant administrator to Daulet;

create user Magzhan;
grant support to Magzhan;

--3
grant Magzhan to Daulet;

--4
revoke delete on accounts from accountant;