--a
select title
from course
where credits > 3

--b
select room_number
from classroom
where (building = 'Packard') or (building = 'Watson')

--c
select title
from course
where dept_name = 'Comp. Sci.'

--d
select course.title
from course, section
where course.course_id = section.course_id and semester = 'Fall'

--e
select name
from student
where (tot_cred > 45) and (tot_cred <90)

--f
select name
from student
where name like '%a' or name like '%e' or name like '%i' or name like '%o' or name like '%u' or name like '%y'

---g
select title
from course
where course_id = 'CS-101'
