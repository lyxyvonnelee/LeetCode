# Write your MySQL query statement below
select name from SalesPerson
where sales_id not in
(select o.sales_id from Company c
join Orders o on  c.com_id = o.com_id and c.name like 'RED')

