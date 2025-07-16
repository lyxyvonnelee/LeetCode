# Write your MySQL query statement below
select p.product_id, product_name from Product p
inner join Sales s on p.product_id = s.product_id
where p.product_id not in (select product_id from Sales where sale_date not between "2019-01-01" and "2019-03-31")
group by p.product_id