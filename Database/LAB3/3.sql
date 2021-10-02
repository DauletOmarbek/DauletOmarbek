--a
select student.name
from student, takes, course
where  student.id = takes.id and course.course_id =  takes.course_id and student.dept_name = course.dept_name and
      (takes.grade = 'A-' or takes.grade = 'A') and student.id NOT in(select student.id from student, takes, course
where  student.id = takes.id and course.course_id =  takes.course_id and student.dept_name = course.dept_name and
      (takes.grade != 'A-' and takes.grade != 'A'))
group by student.name
order by student.name

--b
select instructor.name
from student, advisor, takes, instructor
where student.id = takes.id and advisor.s_id = student.id and instructor.id = advisor.i_id and (takes.grade = 'B-' or takes.grade = 'C+' or takes.grade = 'C' or takes.grade = 'C-' or takes.grade = 'F')


--c
select student.dept_name
from student, takes
where student.id = takes.id and student.dept_name NOT in (select student.dept_name
from student, takes
where student.id = takes.id and (takes.grade = 'C' or takes.grade = 'F' )   )
group by student.dept_name


--d
select instructor.name
from takes, instructor, teaches
where  takes.course_id = teaches.course_id and teaches.id = instructor.id and instructor.name NOT in (select instructor.name
from takes, instructor, teaches
where  takes.course_id = teaches.course_id and teaches.id = instructor.id and (takes.grade = 'A-' or takes.grade = 'B+' or takes.grade = 'B' or takes.grade = 'B-' or takes.grade = 'C+' or takes.grade = 'C' or takes.grade = 'C-' or takes.grade = 'F' ))
group by instructor.name

--e
select course.title
from course, section, time_slot
where time_slot.time_slot_id = section.time_slot_id and section.course_id = course.course_id and time_slot.end_hr < 13
group by course.title