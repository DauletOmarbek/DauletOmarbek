--a
select department.dept_name, AVG(instructor.salary)
from instructor , department
where instructor.dept_name = department.dept_name
group by department.dept_name
order by AVG(instructor.salary);

--b
select building, count(*)
from department, course
where department.dept_name = course.dept_name
group by course.dept_name,department.dept_name
order by count(*) desc
limit 1


--c
select department.dept_name, count(*)
from course, department
where department.dept_name = course.dept_name
group by department.dept_name, course.dept_name
order by count(*)

--d
select student.id, student.name, count(takes.id)  as total
from student, takes
where student.id = takes.id and (course_id like 'CS%')
group by takes.id , student.id
order by count(takes.id)  desc

--e
select name
from instructor
where (dept_name = 'Biology' and dept_name = 'Philosophy') or dept_name = 'Music'

--f
select instructor.name, teaches.year
from teaches, instructor
where teaches.id = instructor.id and teaches.year = 2018 and
      teaches.id NOT in (select teaches.id from teaches, instructor
where teaches.id = instructor.id and teaches.year = 2017)
group by instructor.name, teaches.year
order by instructor.name, teaches.year


