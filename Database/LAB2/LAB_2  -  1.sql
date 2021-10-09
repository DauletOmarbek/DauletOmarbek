
--1 Для DDL
create table  inst(
    ID  char(5),
    name varchar(20),
    dept_name varchar(20),
    salary numeric default 1 CHECK ( salary > 0 )
)


drop table inst



alter table inst add age numeric CHECK ( age > 0)



--2 Для DML
insert into inst (ID, name) values  ('123', 'Daulet');
insert into inst (ID, name) values  ('321', 'Omarbek');


select ID
from inst
where name = 'Omarbek'

update inst
set salary = 50000
where name = 'Daulet'

delete
from  instructor
where name = 'Omarbek'