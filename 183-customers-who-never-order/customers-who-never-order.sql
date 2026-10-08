# Write your MySQL query statement below
# Submitted by noor on 8th oct
SELECT name as Customers FROM Customers 
WHERE id NOT IN (SELECT CustomerID FROM Orders);