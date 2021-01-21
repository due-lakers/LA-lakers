import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report
#from sklearn.metrics import confusion_matrix

stu = pd.read_csv('D:\shahabab\DevCenter\LA-lakers\data\edu-dataset.csv')

#dataset split
x = stu.drop('Class',axis = 1)
x = x.drop('SectionID',axis = 1)
y = stu['Class']
x = pd.get_dummies(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 10)

#Naive Bayes
nb =  GaussianNB()
nb.fit(x_train, y_train)
y_pred = nb.predict(x_test)

print("Accuracy of naive bayes algorithm: ", nb.score(x_test,y_test))