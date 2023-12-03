# Write your MySQL query statement below
SELECT  m.name FROM Employee e
INNER JOIN Employee m
ON e.managerID=m.id
GROUP BY e.managerId
HAVING COUNT(e.id)>=5 
