# Write your MySQL query statement below
select product_name, sum(unit) as unit from Products p
left join (select * from Orders where order_date between "2020-02-01" and "2020-02-29") o
on p.product_id = o.product_id
group by p.product_id
having sum(unit)>=100