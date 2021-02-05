import pandas as pd
import numpy as np
import datetime
from datetime import timedelta

df = pd.read_csv('data/data.csv')
pd.set_option("display.max_rows", 100,
              "display.max_columns", 10,
              "display.max_colwidth", 100,
              "display.width", 100)
a = df['gender'].agg(['min', 'max', np.sum])
t = df.apply(pd.Series.nunique)
gg = df.groupby(['gender'], as_index=False)['gender'].agg('count')
qq = df.groupby(['Topic'], as_index=False)['Topic'].agg('count')
bb = df['Topic'].unique()

aa = df['gender'].value_counts()
cc = df['Topic'].value_counts()
dd = df[['raisedhands']].agg(['min', 'max', 'mean'])
ee = pd.cut(df.where(df['Class'] == 'H')['raisedhands'], [0, 20, 40, 60, 80, 100])
# [142 127  74  71  57]

raisedhands = [df.where(df['Class'] == 'L')['raisedhands'].agg('mean'),
               df.where(df['Class'] == 'M')['raisedhands'].agg('mean'),
               df.where(df['Class'] == 'H')['raisedhands'].agg('mean')]

df['sa'] = np.where(df['StudentAbsenceDays'] == 'Under-7', 0, 1)
StudentAbsenceDays = [df.where(df['Class'] == 'L')['StudentAbsenceDays'].value_counts()['Above-7'],
                      df.where(df['Class'] == 'M')['StudentAbsenceDays'].value_counts()['Above-7'],
                      df.where(df['Class'] == 'H')['StudentAbsenceDays'].value_counts()['Above-7']]

gender_counter = df['gender'].value_counts()
gender = {"name": gender_counter.index.values.tolist(), "value": gender_counter.values.tolist()}
dict = {}
xx = [{'values': gender_counter.values[i], 'name': item} for i, item in enumerate(gender_counter.index.values)]
national_counter = df['NationalITy'].value_counts()
national = {"name": list(national_counter.index.values), "value": list(national_counter)}
xx = [{'values': str(national_counter.values[i]), 'name': item} for i, item in enumerate(national_counter.index.values)]

import util.MongoDb as M

nowday = datetime.datetime.today()
print(nowday.today())
lastweekday = nowday - timedelta(days=7)
print(nowday, lastweekday)
group_dict = {"$group": {"_id": {"time": "$time", "status": "$status"}, "every_status_every_day_count": {"$sum": 1}}}
pipeline = [
    {"$sort": {"createTime": 1}},
    {"$project": {"_id": 1, "createTime": {"$substr": ["$createTime", 0, 10]}}},
    {"$group": {"_id": {"createTime": "$createTime"}, "count": {"$sum": 1}}}
]
ss = M.getCol('lakers', 'predict').aggregate(pipeline)
ccc = []
for info in ss:
    ccc.append([info['_id']['createTime'],info['count']])
