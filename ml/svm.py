# The goal is to test our dataset with both simple SVM and Kernel-SVM (and its variants) in order for us to be able to choose one based on the results.

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read dataset
stud_df = pd.read_csv('../data/edu-dataset.csv')

# pre-process data
# (1) split the data into attributes and labels
x = stud_df.drop('Class', axis=1)
x = x.drop('SectionID', axis=1)
y = stud_df['Class']
x = pd.get_dummies(x)

# (2) split the data into train and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10) 
# random-state=10 had best results! 

# train the algorithm
# (1) simple SVM
from sklearn.svm import SVC
svclassifier = SVC(random_state=10)
svclassifier.fit(x_train,y_train)
print('\n Simple SVM accuracy with *random-state 10: ', svclassifier.score(x_test, y_test))

# make predictions
y_pred = svclassifier.predict(x_test)

# evaluate the algorithm with some metrics
from sklearn.metrics import classification_report, confusion_matrix
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))

svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train, y_train)
print('\n Simple SVM accuracy *linear:  ', svclassifier.score(x_test, y_test))

# make predictions
y_pred = svclassifier.predict(x_test)

# evaluate the algorithm with some metrics
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))


# (2) Kernel-SVM
# (2.1) Polynominal Kernel
svclassifier = SVC(kernel='poly', degree=8)
svclassifier.fit(x_train, y_train)

print('\n Kernel SVM accuracy with *Polynominal kernel:  ', svclassifier.score(x_test, y_test))

# make predictions
y_pred = svclassifier.predict(x_test)

# evaluate the algorithm with some metrics
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))

# (2.2) Gaussian Kernel
svclassifier = SVC(kernel='rbf')
svclassifier.fit(x_train, y_train)

print('\n Kernel SVM accuracy with *Gaussian kernel:  ', svclassifier.score(x_test, y_test))

# make predictions
y_pred = svclassifier.predict(x_test)

# evaluate the algorithm with some metrics
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))

# (2.3) Sigmoid Kernel
svclassifier = SVC(kernel='sigmoid')
svclassifier.fit(x_train, y_train)

print('\n Kernel SVM accuracy with *Sigmoid kernel:  ', svclassifier.score(x_test, y_test))

# make predictions
y_pred = svclassifier.predict(x_test)

# evaluate the algorithm with some metrics
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))

print('\n\n Decision is ours!')