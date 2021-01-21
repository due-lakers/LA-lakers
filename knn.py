#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
warnings.filterwarnings('ignore')

stu=pd.read_csv(r'data\data.csv')




print('raws and columns:',stu.shape)
print('----------------------------------------------')
print('attributes:',stu.columns)

print('----------------------------------------------')
print('(types of attributes):')
print(stu.dtypes)
print('----------------------------------------------')
stu.head()


# In[5]:


print('class',stu['Class'].unique())


# # Transform catagorical attributes into numerical attributes

# In[37]:



num=pd.get_dummies(stu)#turn all attributes into numerical
num.head()


# # Discovering Correlation among attributes

# In[36]:


corr_matrix = num.corr()
corr_matrix["Class_H"].sort_values(ascending=False)


# In[34]:


corr_matrix["Class_M"].sort_values(ascending=False)


# In[35]:


corr_matrix["Class_L"].sort_values(ascending=False)


# # Splitting Dataset

# In[77]:


#dataset split
x=stu.drop('Class',axis=1)
x=x.drop('SectionID',axis=1)
y=stu['Class']
x=pd.get_dummies(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)


# # Logistic Regression

# In[75]:


from sklearn.linear_model import LogisticRegression
#LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
predict_y=lr.predict(x_test)
print('predict',predict_y)
scoreLR=accuracy_score(y_test,predict_y)
scoreLR


# # KNN Classification

# In[78]:


from sklearn.neighbors import KNeighborsClassifier 
np.random.seed(0)

# consider n_neighbors in the range (1,30)
n_neighbors = range(30)
accuracy_list = []

for n in n_neighbors:
    knn = KNeighborsClassifier(n_neighbors=n+1)
    knn.fit(x_train, y_train)                   # fit on the training set
    pred = knn.predict(x_test)                  # predict on the test set
    accuracy = accuracy_score(y_test, pred)     # calculate the accuracy
    accuracy_list.append(accuracy)
    


# In[71]:


plt.plot(range(1,31), accuracy_list)
plt.xlabel('number of neighbors')
plt.ylabel('accuracy')


# In[73]:


#chose n=10
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(x_train, y_train)
knn_pred = knn.predict(x_test)
knn_accuracy = accuracy_score(y_true=y_test, y_pred=knn_pred)
print('The accuracy score of knn is:',knn_accuracy)


# In[ ]:




