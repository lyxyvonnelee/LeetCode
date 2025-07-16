# Write your MySQL query statement below
select distinct reports_to as employee_id, (select name from Employees e1 where e1.employee_id = e.reports_to) as name, count(employee_id) as reports_count, round(avg(age)) as average_age from Employees e
where reports_to is not null
group by reports_to
order by employee_id