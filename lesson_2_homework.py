# -*- coding: utf-8 -*-
"""lesson_2_homework

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mUvBNK0e5eMnWJgad7OhqPHSvkB-idL2
"""

#установка библиотек
!pip install -U psycopg2
!pip install -U plotly

# student11
# student11_password

#проверка подключения PostgreSQL 
import psycopg2
import pandas as pd
#Библиотека ждя визуализации
from IPython.display import HTML
import plotly.express as px


#!введите свои реквизиты!
DB_HOST = '52.157.159.24'
DB_USER = 'student11'
DB_USER_PASSWORD = 'student11_password'
DB_NAME = 'sql_ex_third_stream'

conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_USER_PASSWORD, dbname=DB_NAME)

"""# проверка подключения"""

# task1  (lesson6, дополнительно)
# SQL: Создайте таблицу с синтетическими данными (10000 строк, 3 колонки, все типы int) и заполните ее случайными данными от 0 до 1 000 000. 
# Проведите EXPLAIN операции и сравните базовые операции.

psycopg2.__version__

conn

conn.isexecuting()

cur = conn.cursor()
cur

SQL1 = 'select * from ships'
cur.execute(SQL1)

cur.fetchone()

cur.fetchall()

cur.close()

"""# context manager"""

SQL1 = 'SELECT * FROM ships'

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL1)
        print(curs.fetchone())

SQL1 = 'select * FROM ships'

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL1)
        print(*curs.fetchall(), sep='\n')

"""# выгрузка в pandas"""

SQL1 = 'SELECT * FROM ships'

df = pd.read_sql_query(SQL1, conn)
df

SQL1 = 'SELECT * FROM battles'

df = pd.read_sql_query(SQL1, conn)
df

SQL1 = 'SELECT * FROM classes'

df = pd.read_sql_query(SQL1, conn)
df

SQL1 = 'SELECT * FROM Outcomes'

df = pd.read_sql_query(SQL1, conn)
df

"""# plotly"""

import plotly.express as px

px

"""# задания

* Задание 1: Вывести name, class по кораблям, выпущенным после 1920
"""

SQL1 = 'SELECT name, class FROM ships WHERE launched > 1920'

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 2: Вывести name, class по кораблям, выпущенным после 1920, но не позднее 1942"""

SQL1 = 'SELECT name, class FROM ships WHERE launched > 1920 AND launched <= 1942'

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 3: Какое количество кораблей в каждом классе. Вывести количество и class"""

SQL1 = 'SELECT COUNT(1), class FROM ships GROUP BY class'

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 4: Для классов кораблей, калибр орудий которых не менее 16, укажите класс и страну. (таблица classes)"""

SQL1 = 'SELECT class, country FROM classes WHERE classes.bore >= 16'

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 5: Укажите корабли, потопленные в сражениях в Северной Атлантике (таблица Outcomes, North Atlantic). Вывод: ship."""

SQL1 = "SELECT ship FROM Outcomes WHERE Outcomes.battle = 'North Atlantic' and result = 'sunk'"

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 6: Вывести название (ship) последнего потопленного корабля"""

SQL1 = "SELECT ship FROM Outcomes INNER JOIN battles ON Outcomes.battle = battles.name WHERE Outcomes.result = 'sunk' ORDER BY battles.date DESC LIMIT 1"

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 7: Вывести название корабля (ship) и класс (class) последнего потопленного корабля"""

SQL1 = """
SELECT Outcomes.ship, ships.class FROM Outcomes 
INNER JOIN battles ON Outcomes.battle = battles.name 
INNER JOIN ships ON Outcomes.ship = ships.name 
WHERE Outcomes.result = 'sunk' 
ORDER BY battles.date DESC 
LIMIT 1
"""

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 8: Вывести все потопленные корабли, у которых калибр орудий не менее 16, и которые потоплены. Вывод: ship, class"""

SQL1 = """
SELECT Outcomes.ship, ships.class 
FROM Outcomes 
INNER JOIN battles ON Outcomes.battle = battles.name 
INNER JOIN ships ON Outcomes.ship = ships.name 
INNER JOIN classes ON ships.class = classes.class 
WHERE Outcomes.result = 'sunk' AND classes.bore >= 16
"""

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 9: Вывести все классы кораблей, выпущенные США (таблица classes, country = 'USA'). Вывод: class"""

SQL1 = """
SELECT class 
FROM classes
WHERE country = 'USA'
"""

df = pd.read_sql_query(SQL1, conn)
df

"""* Задание 10: Вывести все корабли, выпущенные США (таблица classes & ships, country = 'USA'). Вывод: name, class"""

SQL1 = """
SELECT ships.name, ships.class 
FROM ships 
INNER JOIN classes ON classes.class = ships.class 
WHERE classes.country = 'USA'
"""

df = pd.read_sql_query(SQL1, conn)
df







