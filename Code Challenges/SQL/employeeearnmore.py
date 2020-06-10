not done
# Write your MySQL query statement below

# (User) Problem
# We know/ We have: just one table with all employees, managers, salaries
# We need / We don't have: which employees earn more than their managers
# We must / requirements:
# return only the name of those employees who earn more than their manager
# 
# Solution (Product)
# use conditionals?
# note: conditionals vs. joins
# note: aliasing

SELECT Name AS Employee
from Employee
WHERE ManagerId = 3;


# SELECT Name AS Employee
# from Employee
# WHERE ManagerId = 3;


# SELECT Name, dpartment_id, salary,
#        CASE dpartment_id WHEN 50 THEN 1.5*salary
#                          WHEN 12 THEN 2.0*salary
#        ELSE salary
#        END "REVISED SALARY"
# FROM Employee;
