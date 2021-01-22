import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

stud_df = pd.read_csv('../data/edu-dataset.csv')

#dataset split
x = stud_df.drop('Class', axis = 1)
x = x.drop('SectionID', axis = 1)
y = stud_df['Class']
x = pd.get_dummies(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 10)

#Naive Bayes
nb =  GaussianNB()
nb.fit(x_train, y_train)
y_pred = nb.predict(x_test)

print("\n Accuracy of naive bayes algorithm: ", nb.score(x_test,y_test))