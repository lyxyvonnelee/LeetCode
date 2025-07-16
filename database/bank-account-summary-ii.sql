# Write your MySQL query statement below
select NAME, sum(amount) as BALANCE from Users u
left join Transactions t on u.account = t.account
group by u.account
having sum(amount)>10000