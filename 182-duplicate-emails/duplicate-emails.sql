# Write your MySQL query statement below
# submitted on 8th oct by noor
select email from person
group by email
having count(email) > 1 