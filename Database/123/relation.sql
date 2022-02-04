CREATE table Transaction(
    ID int NOT NULL PRIMARY KEY,
    Customer_ID int NOT NULL,
    Product_ID int NOT NULL,
    Date_tr date NOT NULL,
    Season varchar(50),
    Region varchar(50),
    price_of_purchase int
);

insert into Transaction(ID, Customer_ID, Product_ID, Date_tr, Season, Region, price_of_purchase)
VALUES ('1', '6', '2', '2021-11-11', 'Autumn', 'North', '20000'),
       ('2', '5', '1', '2021-09-30', 'Autumn', 'West', '120000'),
       ('3', '4', '6', '2021-08-23', 'Summer', 'East', '150000'),
       ('4', '1', '5', '2021-08-15', 'Summer', 'South', '200000'),
       ('5', '7', '4', '2021-07-12', 'Summer', 'North', '260000'),
       ('6', '2', '3', '2021-07-30', 'Summer', 'South', '360000'),
       ('7', '8', '7', '2021-06-28', 'Summer', 'West', '240000'),
       ('8', '3', '8', '2021-05-17', 'Summer', 'East', '50000'),
       ('9', '9', '9', '2021-05-17', 'Spring', 'North', '10000'),
       ('10', '10', '10', '2021-04-25', 'Spring', 'West', '15000');


CREATE table Company(
    ID int NOT NULL PRIMARY KEY,
    Name varchar(50) NOT NULL,
    Address varchar(50) NOT NULL,
    Index varchar(50) NOT NULL
);

INSERT INTO Company(ID, Name, Address, Index)
VALUES ('100', 'Mechta', 'Tole-Bi', '100123'),
       ('101', 'Technodom', 'Abay', '101123'),
       ('102', 'Alser', 'Raimbek', '102123');

CREATE table Shipper(
    Tracking_number int NOT NULL PRIMARY KEY,
    Product_ID int NOT NULL,
    Phone_number varchar(11)
);

INSERT INTO Shipper(Tracking_number, Product_ID, Phone_number)
VALUES ('5', '1', '87777145876'),
       ('6', '8', '87774785322'),
       ('8', '6', '87774856998'),
       ('10', '7', '87774788547'),
       ('7', '9', '87774457874');

CREATE table Storage(
    storage_id int primary key ,
    Product_ID int[],
    Quantity int NOT NULL,
    Last_update_date date NOT NULL
);

INSERT INTO Storage(storage_id, Product_ID, Quantity, Last_update_date)
VALUES ('1', '{1, 2, 3}', '25', '2021-07-02'),
       ('2', '{4, 5,6}', '45', '2021-06-30'),
       ('3', '{7, 8, 9}', '80', '2021-12-06');



CREATE table Checking(
    ID int NOT NULL PRIMARY KEY,
    Date_of_inv date NOT NULL,
    Product_ID int NOT NULL,
    Employee_ID int NOT NULL
);

INSERT INTO Checking(ID, Date_of_inv, Product_ID, Employee_ID)
VALUES ('1001', '2021-04-04', '4', ''),
       ('1002', '2021-02-20', '8', ''),
       ('1003', '2021-01-30', '9', ''),
       ('1004', '2020-12-25', '6', '');

CREATE table Purchase_Order_for_parts(
    ID int NOT NULL PRIMARY KEY,
    Product_ID int NOT NULL,
    Name varchar(50) NOT NULL,
    Quantity varchar(50) NOT NULL,
    Purchased_date date NOT NULL,
    Cost int NOT NULL
);

CREATE table Suppliers(
    ID int NOT NULL PRIMARY KEY,
    Name varchar(50) NOT NULL,
    Address varchar(50) NOT NULL,
    Phone_number varchar(11) NOT NULL,
    Order_ID int NOT NULL
);

CREATE table Factory(
    ID int NOT NULL PRIMARY KEY,
    Product_ID int NOT NULL,
    Location varchar(50) NOT NULL
);