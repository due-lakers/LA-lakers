import pandas as pd
from sklearn.naive_bayes import GaussianNB

stud_df = pd.read_csv('../data/edu-dataset.csv')

# split dataset
x = stud_df.drop('Class', axis = 1)
x = x.drop('SectionID', axis = 1)
y = stud_df['Class']
x = pd.get_dummies(x)

# pre-process data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 10)

# train Naive-Bayes
nb =  GaussianNB()
nb.fit(x_train, y_train)
y_pred = nb.predict(x_test)

print("\n Accuracy of Naive-Bayes algorithm: ", nb.score(x_test, y_test))

# do some predictions
y_pred = nb.predict(x_test)

# evaluate the algorithm with some metrics
from sklearn.metrics import classification_report, confusion_matrix
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))

# train SVM linear
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train, y_train)
print('\n Simple SVM accuracy *linear:  ', svclassifier.score(x_test, y_test))

# make predictions
y_pred = svclassifier.predict(x_test)

# evaluate the algorithm with some metrics
print('\n', confusion_matrix(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))