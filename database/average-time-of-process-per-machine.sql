# Write your MySQL query statement below
select machine_id,
round((select avg(a1.timestamp) from Activity a1 where a1.activity_type="end" and a1.machine_id=a.machine_id)-(select avg(a2.timestamp) from Activity a2 where a2.activity_type="start" and a2.machine_id=a.machine_id),3)
as processing_time from Activity a
group by machine_id
