# -*- coding: utf-8 -*-
"""lesson_8_homework

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HMqx-26W9EanrOoZLc861yIRRCZJwP2L

# task1  (lesson8)
* oracle: https://leetcode.com/problems/department-top-three-salaries/
"""

# в режиме oracle - не смог запустить оконные фукнции
# поэтому ограничение количества делал вручную

WITH salary_by_department AS
(
    SELECT DISTINCT departmentId, salary
    FROM Employee
    GROUP BY departmentId, salary
    ORDER BY departmentId ASC, salary DESC
)
,
salary_by_department_top_3 AS
(
    SELECT departmentId, salary
    FROM salary_by_department s_1
    WHERE 
    (
        SELECT COUNT(1) 
        FROM salary_by_department s_2
        WHERE 
            (s_2.salary >= s_1.salary) AND
            (s_2.departmentId = s_1.departmentId)
    ) <= 3
)
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary
FROM salary_by_department_top_3
INNER JOIN Department
ON salary_by_department_top_3.departmentId = Department.id
INNER JOIN Employee
ON salary_by_department_top_3.salary = Employee.salary

"""# task2  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/17
"""

WITH member_payment AS 
(
    SELECT family_member, SUM(amount * unit_price) AS costs
    FROM Payments
    WHERE year(date) = 2005
    GROUP BY family_member
)
SELECT FamilyMembers.member_name, FamilyMembers.status, member_payment.costs
FROM member_payment
INNER JOIN FamilyMembers
ON member_payment.family_member= FamilyMembers.member_id

"""# task3  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/13
"""

select name
from Passenger
group by name
HAVING count(name) >= 2

"""# task4  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/38
"""

SELECT COUNT(1) as count
FROM Student
WHERE first_name = 'Anna'

"""# task5  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/35
"""

SELECT COUNT(DISTINCT classroom) AS count
FROM Schedule
WHERE date = '2019-09-02'

"""# task6  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/38
"""

SELECT COUNT(1) as count
FROM Student
WHERE first_name = 'Anna'

"""# task7  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/32
"""

SELECT FLOOR(AVG(FLOOR((now() - (birthday)) / 10000000000))) AS age
FROM FamilyMembers

"""# task8  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/27
"""

SELECT good_type_name, SUM(amount*unit_price) AS costs
FROM Payments
INNER JOIN Goods
ON Payments.good = Goods.good_id
INNER JOIN GoodTypes
ON Goods.type = GoodTypes.good_type_id
WHERE YEAR(date) = 2005
GROUP BY good_type_name

"""# task9  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/37
"""

SELECT FLOOR(MIN((date(now()) - date(birthday)) / 10000)) as year
FROM Student

"""# task10  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/44
"""

SELECT MAX(FLOOR(((date(now()) - date(birthday)) / 10000))) as max_year
FROM Class
INNER JOIN Student_in_class
ON Class.id = Student_in_class.class
INNER JOIN Student
ON Student_in_class.student = Student.id
WHERE name LIKE '10%'

"""# task11 (lesson8)
* https://sql-academy.org/ru/trainer/tasks/20
"""

SELECT status, member_name, SUM(amount * unit_price) AS costs
FROM FamilyMembers
INNER JOIN Payments
ON FamilyMembers.member_id = Payments.family_member
INNER JOIN Goods
ON Payments.good= Goods.good_id
INNER JOIN GoodTypes
ON Goods.type= GoodTypes.good_type_id
WHERE good_type_name = 'entertainment'
GROUP BY status, member_name

"""# task12  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/55
"""

WITH company_trips AS 
(
    SELECT company, COUNT(1) as trips_count
    FROM Company
    INNER JOIN Trip
    ON Company.id = Trip.company
    GROUP BY company
),
min_company_trips AS 
(
    SELECT *
    FROM company_trips 
    WHERE trips_count = (SELECT MIN(trips_count) FROM company_trips)
)    
DELETE 
FROM Company
WHERE id IN (SELECT company FROM min_company_trips )

"""# task13  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/45
"""

WITH classroom_count AS
(
    SELECT classroom, COUNT(1) as classroom_count
    FROM Schedule
    GROUP BY classroom
),
max_classroom_count AS
(
    SELECT MAX(classroom_count) as max_classroom_count
    FROM classroom_count 
)
SELECT classroom
FROM classroom_count 
WHERE classroom_count = (SELECT max_classroom_count FROM max_classroom_count)

"""# task14  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/43
"""

SELECT last_name
FROM Teacher
INNER JOIN Schedule
ON Teacher.id = Schedule.teacher
INNER JOIN Subject
ON Schedule.subject = Subject.id
WHERE name = 'Physical Culture'
ORDER BY last_name

"""# task15  (lesson8)
* https://sql-academy.org/ru/trainer/tasks/63 
"""

# вроде сделал все по заданию, но тренажер не принимает результат



WITH fio AS 
(
    SELECT CONCAT(UPPER(SUBSTRING(last_name, 1, 1)), LOWER(SUBSTRING(last_name, 2)), '.', SUBSTRING(first_name, 1, 1), '.', SUBSTRING(middle_name, 1, 1), '.') AS name
    FROM Student
)    
SELECT name FROM fio 
ORDER BY name