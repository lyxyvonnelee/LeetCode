# Write your MySQL query statement below
SELECT
    *
FROM
    Users
WHERE
    mail regexp '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com'
