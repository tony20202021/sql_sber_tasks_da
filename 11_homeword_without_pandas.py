# -*- coding: utf-8 -*-
"""11_homeword_without_pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O13TyY0YFg85cPhRZNFjNze7q70iv2h2

# REBOOT_DA
## 11_homeword_without_pandas
### Михалев Антон
"""

from IPython.display import YouTubeVideo
YouTubeVideo('lyDLAutA88s', width=800, height=300)

# 1. Посмотрите видео Дэвида Бизли про всроенные инструменты Python
# 2. Попробуйте используя встроенные инструменты Python проанизировать таблицу из файла "Vacancy.csv"
# 3. Попробуйте ответить на вопросы:
# Сколько вакансий, которые вам нравятся?
# Насколько свежие эти вакансии?
# Сколько вакансий с позициями на которых вы работаете?
# Сколько вакансий для аналатика данных?
# Сколько вакансий для аналитика данных с использованием Python?

# В задании важно не использовать pandas и numpy, а встроенные инструменты python
# Counter, CSV, defaultdict, sorted

from google.colab import drive
drive.mount('/content/drive')

!ls "./drive/MyDrive/Colab Notebooks/20_REBOOT_DA/"

colab_path = "./drive/MyDrive/Colab Notebooks/20_REBOOT_DA/"
colab_path

import csv

import sys

csv.field_size_limit(sys.maxsize)

vacs = list(csv.DictReader(open(colab_path + 'vacancy.csv')))

len(vacs)

vacs[0]

"""# Сколько вакансий, которые вам нравятся?
* допустим, мне нравятся вакансии, в названии которых есть слово "senior" :)
"""

result = [v for v in vacs if ('Senior'.upper() in v['vactitle'].upper())]
len(result), result[:2]

"""# Насколько свежие эти вакансии?"""

from datetime import datetime

[(datetime.now() - datetime.strptime(v['vacdate'], '%Y-%m-%d')).days for v in result][:2]



"""# Сколько вакансий с позициями на которых вы работаете?
* допустим, я работаю программистом на Дельфи :)
"""

result = [v 
          for v in vacs 
          if (('delphi'.upper() in v['vactitle'].upper())) 
            or (('delphi'.upper() in v['vacdescription'].upper()))
          ]
len(result), result[:2]

len(result[0]['vacdescription'])

pos = (result[0]['vacdescription'].upper()).find('delphi'.upper())
pos

result[0]['vacdescription'][pos - 50: pos + 50]

"""# Сколько вакансий для аналатика данных?

"""

query = 'data analyst'

result = [v 
          for v in vacs 
          if ((query.upper() in v['vactitle'].upper())) 
            # or ((query.upper() in v['vacdescription'].upper()))
          ]
len(result), result[:2]



"""# Сколько вакансий для аналитика данных с использованием Python?"""

query_1 = 'data analyst'
query_2 = 'python'

result = [v 
          for v in vacs 
          if (
              ((query_1.upper() in v['vactitle'].upper())) 
        #    or ((query_1.upper() in v['vacdescription'].upper()))
          )
          and
          (
              ((query_2.upper() in v['vactitle'].upper())) 
        #    or ((query_2.upper() in v['vacdescription'].upper()))
          )
          ]
len(result), result[:2]

