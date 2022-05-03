# -*- coding: utf-8 -*-
"""13_homework_Cluster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vLE-fPtnndZFqq8X6S6m3V-F6S5hVEGL

# Задание
"""

# from google.colab import drive
# drive.mount('/content/drive')

"""### Основная часть

* Попробовать построить графики из тех, что были на уроке по Seaborn и Matplotlib
* Важно чтобы у каждого из графиков был как минимум один в комментариях или markdown

### Дополнительная часть

* Некоторые данные представлены в агрегированном в виде в разном временном размере. Если вам нужны дополнительные переменные, то добавьте их в датасет.

* Опишите данную вам выборку, а так же кластеризуйте данные с помощь инструментов Python (количество кластеров на ваше усмотрение) и опишите полученные кластеры ( например, в первом кластере представлены клиенты с таким-то поведением или продуктовым наполнением).

* Для выполнения работы, пожалуйста, используйте Python. Задание мы ждем выполненным в Jupyter notebook с соответствующими комментариями.

# Описания полей

* age	возраст
* gender	пол repexc_date
* city_type	Тип города проживания клиента
* full_mob	Длительность взаимоотношений с банком

* ml_balance	ипотека
* cl_balance_0m	потребительский кредит
* loan_balance_0m	все кредиты

* td_balance_0m	депозит
* casa_balance_0m	счета

* dc_trx_cnt	количество трат по картам
* dc_trx_sum	сумма трат по картам
* Avg_trx	средний размер транзакции
* avgtrx_to_balance	


* min_casa_balance_1q	показатели по счетам за квартал
* max_casa_balance_1q	
* avg_casa_balance_1Y	показатели по счетам за год

* min_td_balance_1q	
* max_td_balance_1q	
* avg_td_balance_1Y

* min_loan_balance_1q	
* max_loan_balance_1q	
* avg_loan_balance_1Y

* min_cl_balance_1q	
* max_cl_balance_1q	
* avg_cl_balance_1Y	
* loan_to_deposit	

* income	доход клиента
* nbi	доход от клиента без OPEX
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from tqdm.auto import tqdm

"""# скачиваем датасет"""

!wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Xankd_YIM2ufCvUiCWk4qPm0j7um2mT8' -O test_cluster.csv

!ls

df = pd.read_csv('test_cluster.csv', encoding='cp1251', sep=';')
df
# .head()

df.info()

"""# смотрим распределение значений"""

df['age'].hist()

df['Avg_trx'].hist(log=True)



"""# смотим разброс минимум-максимум по колонке "возраст""""

df['age'].min(), df['age'].max()

df['age'].value_counts()

"""# разбиваем на 10 кластеров по возрасту, равномерно, от минимума, до максимума"""

N_BINS = 10
N_BINS

df['age_bin'] = ((N_BINS * df['age']) / df['age'].max()).astype(int)
df

"""# смотрим распределение среднего дохода по кластерам возраста"""

df.groupby(by=['age_bin'])['income'].mean().plot.bar()

"""# посмотрим тройное распределение возраст-доход-пол"""

df['income'].sort_values()

df_not_null = df[df['income'] > 0]
df_not_null

np.log(df_not_null['income']).value_counts()

np.log(df_not_null['income']).hist()

df_not_null['gender'].value_counts()

gender_dict = {key: index for index, key in enumerate(df_not_null['gender'].unique())}
gender_dict

df_not_null['gender_num'] = df_not_null['gender'].apply(lambda x: gender_dict[x])
df_not_null

fig, ax = plt.subplots(1, 1, figsize=(19, 8))

ax.set_title('пол: {}'.format(str(gender_dict)))
ax.set_xlabel('возраст')
ax.set_ylabel('доход (логарифмированный)')

sc = ax.scatter(x=df_not_null['age'], y=np.log(df_not_null['income']), c=df_not_null['gender_num'])

plt.colorbar(sc)
plt.show()

