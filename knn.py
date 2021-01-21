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
print (1)
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
from sklearn.preprocessing import LabelEncoder


plt.plot(range(1,31), accuracy_list)
plt.xlabel('number of neighbors')
plt.ylabel('accuracy')


# In[73]:

train_data = pd.read_csv("data/data.csv")
train_Y = train_data["Class"]
train_X = train_data.drop(columns=['Class'])
# train_X = train_data.drop(columns=['NationalITy','ParentschoolSatisfaction','StudentAbsenceDays','Class','GradeID','SectionID','Topic','Relation','Semester','StageID','PlaceofBirth'])
def cope_X(df):
    genderEncoder = LabelEncoder()
    NationEncoder = LabelEncoder()
    BirthEncoder = LabelEncoder()
    StagedEncoder = LabelEncoder()
    GradeEncoder = LabelEncoder()
    SectionsEncoder = LabelEncoder()
    TopicsEncoder = LabelEncoder()
    SemesterEncoder = LabelEncoder()
    RelationEncoder = LabelEncoder()
    ParentAnsweringSurveyEncoder = LabelEncoder()
    ParentschoolSatisfactionEncoder = LabelEncoder()
    StudentAbsenceDaysEncoder = LabelEncoder()

    df.gender = genderEncoder.fit_transform(df.gender)
    df.NationalITy = NationEncoder.fit_transform(df.NationalITy)
    df.PlaceofBirth = BirthEncoder.fit_transform(df.PlaceofBirth)
    df.StageID = StagedEncoder.fit_transform(df.StageID)
    df.GradeID = GradeEncoder.fit_transform(df.GradeID)
    df.SectionID = SemesterEncoder.fit_transform(df.SectionID)
    df.Topic  = TopicsEncoder.fit_transform(df.Topic)
    df.Semester = SemesterEncoder.fit_transform(df.Semester)
    df.Relation = RelationEncoder.fit_transform(df.Relation)
    df.ParentAnsweringSurvey  = ParentschoolSatisfactionEncoder.fit_transform(df.ParentAnsweringSurvey)
    df.ParentschoolSatisfaction = ParentschoolSatisfactionEncoder.fit_transform(df.ParentschoolSatisfaction)
    df.StudentAbsenceDays = StagedEncoder.fit_transform(df.StudentAbsenceDays)
    return df

train_X = cope_X(train_X).values
labelEncoder = LabelEncoder()
train_Y = labelEncoder.fit_transform(train_Y)
X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=.3, random_state=0)



#chose n=10
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
knn_accuracy = accuracy_score(y_true=y_test, y_pred=knn_pred)
print('The accuracy score of knn is:',knn_accuracy)
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
krange = range(1,33)
ks = []
bs = []
for l in krange:
    knn = KNeighborsClassifier(n_neighbors=l)
    knn.fit(X_train, y_train)
    scores = cross_val_score(knn,X_train,y_train,cv=5,scoring='accuracy')
    knn_pred = knn.predict(X_test)
    ks.append(scores.mean())
    bs.append(accuracy_score(y_true=y_test, y_pred=knn_pred))
    # print("%d-%f" %(l,clf.score(X_train, y_train)))
plt.subplot(1,2,1)
plt.plot(krange,ks)
plt.xlabel('Value')
plt.ylabel('Cross-Validated Accuracy')
plt.subplot(1,2,2)
plt.plot(krange,bs)
plt.xlabel('bsValue')
plt.ylabel('Accuracy')
plt.show()

# In[ ]:




