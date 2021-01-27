#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stu=pd.read_csv(r'C:\Users\ZDX\Desktop\Sheet1.csv')
stu.head()


# In[ ]:





# In[47]:


num=pd.get_dummies(stu)#turn all attributes into numerical

corrMatrix=num.corr()
corrMatrix
sns.heatmap(corrMatrix)


# In[ ]:




