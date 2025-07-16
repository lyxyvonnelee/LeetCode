# Write your MySQL query statement below
# select employee_id, 
# (select department_id from Employee e1 
# where (e1.primary_flag='Y' and e1.employee_id=e.employee_id) or (count(e.employee_id)=1 and e1.employee_id=e.employee_id))
# as department_id 
# from Employee e
# group by e.employee_id
# having department_id is not null

SELECT employee_id, department_id FROM Employee WHERE primary_flag = 'Y'
UNION
SELECT employee_id, department_id FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1