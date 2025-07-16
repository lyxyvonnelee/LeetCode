# Write your MySQL query statement below
select user_id, 
(select max(time_stamp) from logins l1 where time_stamp like "2020%" and l.user_id=l1.user_id) as last_stamp 
from logins l
group by user_id
having last_stamp is not null