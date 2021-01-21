# read dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline

#stu=pd.read_csv('edu-dataset.csv')
bankdata = pd.read_csv("bill_authentication.csv")

# exploratory data analysis
#stu.shape
#stu.head()
bankdata.shape
bankdata.head()

# process data
# (1) dividing the data into attributes and labels and
X = bankdata.drop('Class', axis = 1)
y = bankdata['Class']

# (2) dividing the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

# train the model
from sklearn.svm import SVC
svclassifier = SVC(kernel = 'linear')
svclassifier.fit(X_train, y_train)

# make predictions
y_pred = svclassifier.predict(X_test)

# evaluate the algorithm
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))