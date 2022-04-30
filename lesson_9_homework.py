# -*- coding: utf-8 -*-
"""lesson_9_homework

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s4UdPniaoO5GH0vekwUipyzBXtu7R3lK

# task1  (lesson9)
* oracle: https://www.hackerrank.com/challenges/the-report/problem
"""

WITH students_grades AS
(
    SELECT Name, Grade, Marks
    FROM Students, Grades 
    WHERE 
        (Students.Marks >= Grades.Min_Mark) AND
        (Students.Marks <= Grades.Max_Mark)
) 
SELECT Name, Grade, Marks
FROM students_grades
WHERE Grade >= 8
UNION
SELECT NULL, Grade, Marks
FROM students_grades
WHERE Grade < 8
ORDER BY Grade DESC, Name, Marks
;

"""# task2  (lesson9)
* oracle: https://www.hackerrank.com/challenges/occupations/problem
"""

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
WITH name_number AS
(
    SELECT Name, Occupation, ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY Occupation, Name) AS rn
    FROM OCCUPATIONS 
),
max_name_number AS
(
    SELECT MAX(rn)
    FROM name_number 
), 
unique_number AS
(
    SELECT DISTINCT rn
    FROM name_number
    ORDER BY rn
), 
all_actors AS
(
    SELECT Name, Occupation, rn
    FROM name_number
    WHERE Occupation = 'Actor'
    ORDER BY Name
),
all_doctors AS
(
    SELECT Name, Occupation, rn
    FROM name_number
    WHERE Occupation = 'Doctor'
    ORDER BY Name
),
all_professors AS
(
    SELECT Name, Occupation, rn
    FROM name_number
    WHERE Occupation = 'Professor'
    ORDER BY Name
),
all_singers AS
(
    SELECT Name, Occupation, rn
    FROM name_number
    WHERE Occupation = 'Singer'
    ORDER BY Name
)
SELECT 
    all_doctors.Name, 
    all_professors.Name,
    all_singers.Name, 
    all_actors.Name
FROM unique_number
FULL JOIN all_doctors
ON (unique_number.rn = all_doctors.rn)
FULL JOIN all_professors
ON (unique_number.rn = all_professors.rn)
FULL JOIN all_singers
ON (unique_number.rn = all_singers.rn) 
FULL JOIN all_actors
ON (unique_number.rn = all_actors.rn) 
;



"""# task3  (lesson9)
* oracle: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
"""

SELECT DISTINCT city
FROM STATION 
WHERE LOWER(SUBSTR(city, 1, 1)) not in ('a', 'e', 'i', 'o', 'u')
;

"""# task4  (lesson9)
* oracle: https://www.hackerrank.com/challenges/weather-observation-station-10/problem
"""

SELECT DISTINCT city
FROM STATION 
WHERE LOWER(SUBSTR(city, -1, 1)) not in ('a', 'e', 'i', 'o', 'u')
;

"""# task5  (lesson9)
* oracle: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
"""

SELECT DISTINCT city
FROM STATION 
WHERE 
    (LOWER(SUBSTR(city, 1, 1)) not in ('a', 'e', 'i', 'o', 'u')) OR
    (LOWER(SUBSTR(city, -1, 1)) not in ('a', 'e', 'i', 'o', 'u'))
;

"""# task6  (lesson9)
* oracle: https://www.hackerrank.com/challenges/weather-observation-station-12/problem
"""

SELECT DISTINCT city
FROM STATION 
WHERE 
    (LOWER(SUBSTR(city, 1, 1)) not in ('a', 'e', 'i', 'o', 'u')) AND
    (LOWER(SUBSTR(city, -1, 1)) not in ('a', 'e', 'i', 'o', 'u'))
;

"""# task7  (lesson9)
* oracle: https://www.hackerrank.com/challenges/salary-of-employees/problem
"""

SELECT name
FROM Employee 
WHERE 
    (salary > 2000) AND
    (months < 10)
ORDER BY employee_id ASC
;

"""# task8  (lesson9)
* oracle: https://www.hackerrank.com/challenges/the-report/problem 
"""

WITH students_grades AS
(
    SELECT Name, Grade, Marks
    FROM Students, Grades 
    WHERE 
        (Students.Marks >= Grades.Min_Mark) AND
        (Students.Marks <= Grades.Max_Mark)
) 
SELECT Name, Grade, Marks
FROM students_grades
WHERE Grade >= 8
UNION
SELECT NULL, Grade, Marks
FROM students_grades
WHERE Grade < 8
ORDER BY Grade DESC, Name, Marks
;