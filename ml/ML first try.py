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

stu=pd.read_csv('../data/edu-dataset.csv')




print('raws and columns:', stu.shape)
print('----------------------------------------------')
print('attributes:', stu.columns)

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
print('\n The accuracy score of knn is:',knn_accuracy)


# In[8]:


from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score

#dataset split

x=stu.drop('Class',axis=1)
x=x.drop('SectionID',axis=1)
y=stu['Class']
x=pd.get_dummies(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)



nb =  GaussianNB()


nb.fit(x_train, y_train)
y_pred=nb.predict(x_test)

print("\n Accuracy of naive bayees algorithm: ",nb.score(x_test,y_test))


# In[9]:


from sklearn.svm import SVC

svm=SVC(random_state=1)
svm.fit(x_train,y_train)


svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train, y_train)

#accuracy svm
print("accuracy of svm algorithm: ",svm.score(x_test,y_test))

#new accuracy svm
print("accuracy of svm algorithm (NEW): ",svclassifier.score(x_test,y_test))


# make predictions with SVM
print ('\n make predictions with SVM \n svclassifier.predict(x_test) \n')
y_pred = svclassifier.predict(x_test)
print('y_test ', y_test.shape)
print('y_pred ', y_pred.shape)

# evaluate the SVM algorithm using confusion matrix
print('\n \n SVM evaluation')

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print('\n \n Go to ml/svm.py for even better results and more info \n')


# In[ ]:




