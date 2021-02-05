#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stu=pd.read_csv('data/Cleaned_Sheet1.csv')
stu.head()


# In[ ]:




# In[47]:

num=pd.get_dummies(stu)#turn all attributes into numerical
sns.heatmap(num)
num.head()
plt.show()
print(num.shape)
# In[ ]:




