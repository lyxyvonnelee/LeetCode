# Write your MySQL query statement below
select s.student_id , student_name, sub.subject_name , count(e.subject_name) as attended_exams from Students s
join Subjects sub
left join Examinations e on s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, sub.subject_name
ORDER BY s.student_id, sub.subject_name