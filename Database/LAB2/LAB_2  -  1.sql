
--1 Для DDL
create table  instructor(
    ID  char(5),
    name varchar(20),
    dept_name varchar(20),
    salary numeric default 1 CHECK ( salary > 0 )
)


drop table instructor



alter table instructor add age numeric CHECK ( age > 0)



--2 Для DML
insert into instructor (ID, name) values  ('123', 'Daulet');
insert into instructor (ID, name) values  ('321', 'Omarbek');


select ID
from instructor
where name = 'Omarbek'

update instructor
set salary = salary + 50000
where name = 'Daulet'

delete
from  instructor
where name = 'Omarbek'