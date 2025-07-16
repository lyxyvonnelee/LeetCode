# Write your MySQL query statement below
# select if(count(num)=1, num, NULL) as num from MyNumbers
# Group by num
# having count(*)=1
# order by count(*), num desc limit 1

select if(count(num)=1, num, NULL) as num from MyNumbers
Group by num
order by count(*), num desc limit 1
