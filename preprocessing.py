import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import pickle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

df = pd.read_csv('data\data.csv',engine='python',sep=',')
df.head()
df['Score'] = df['Class']
df['Score'].loc[df.Score == 'Low-Level'] = 0.0
df['Score'].loc[df.Score == 'Middle-Level'] = 1.0
df['Score'].loc[df.Score == 'High-Level'] = 2.0
continuous_subset = df.iloc[:, 9:13]

continuous_subset['gender'] = np.where(df['gender'] == 'M', 1, 0)
continuous_subset['Parent'] = np.where(df['Relation'] == 'Father', 1, 0)
# print(continuous_subset)
X = np.array(continuous_subset).astype('float64')
y = np.array(df['Score'])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)

clf = SVC(C=0.8, kernel='rbf', gamma=1, decision_function_shape='ovo')
clf.fit(X_train, y_train.ravel())
scores = cross_val_score(clf, X_train, y_train, cv=10, scoring='accuracy')
print('cross_val_score:',scores.mean())
print('clf.score:',clf.score(X_train, y_train))
y_hat = clf.predict(X_train)
krange = range(1,10)
ks = []
for l in krange:
    clf = SVC(C=0.8+l*0.1, kernel='rbf', gamma=l, decision_function_shape='ovo')
    scores = cross_val_score(clf,X_train,y_train,cv=10,scoring='accuracy')
    ks.append(scores.mean())

plt.plot(krange,ks)
plt.xlabel('Value')
plt.ylabel('Cross-Validated Accuracy')
plt.show()
count = 0
for i in range(len(X_train)):
    # print(y_hat[i])
    # print(X_train[i])
    if y_hat[i] != y_train[i]:
        count += 1
        print(y_train[i])
        print("%d/%d" % (count,len(X_train)))

# evaluate the algorithm
print(confusion_matrix(y_train, y_hat))
print(classification_report(y_train, y_hat))
# ---
# s=pickle.dumps(clf)
# f=open('model/svm.model', "wb+")
# f.write(s)
# f.close()
# print ("Done\n")
#
#
