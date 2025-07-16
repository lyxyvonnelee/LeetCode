# Write your MySQL query statement below
select w.id from Weather w, Weather h
where datediff(w.recordDate, h.recordDate) = 1 and w.temperature > h.temperature