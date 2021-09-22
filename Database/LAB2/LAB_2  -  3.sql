create table students(
     full_name varchar(50) PRIMARY KEY ,
     age numeric(2) NOT NULL ,
     birth_date varchar(10) NOT NULL,
     gender varchar(10) NOT NULL,
     average_grade numeric NOT NULL,
     information_about_yourself varchar NOT NULL,
     dormitory boolean default false,
     additional_info varchar NOT NULL
)

create table instructors(
    full_name varchar(50) PRIMARY KEY ,
    speaking_languages varchar(100) NOT NULL,
    experience numeric(2) NOT NULL,
    remote_lessons boolean default false
)

create table lesson(
    title varchar(30),
    instructor varchar REFERENCES instructors(full_name),
    studying_students varchar REFERENCES students(full_name),
    room_number numeric
)


