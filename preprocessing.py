import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split

df = pd.read_csv('D:\Projects\LA-lakers\data\data.csv',engine='python',sep=',')
df.head()
df['TotalQ'] = df['Class']
df['TotalQ'].loc[df.TotalQ == 'Low-Level'] = 0.0
df['TotalQ'].loc[df.TotalQ == 'Middle-Level'] = 1.0
df['TotalQ'].loc[df.TotalQ == 'High-Level'] = 2.0
continuous_subset = df.iloc[:, 9:13]

continuous_subset['gender'] = np.where(df['gender'] == 'M', 1, 0)
continuous_subset['Parent'] = np.where(df['Relation'] == 'Father', 1, 0)
print(continuous_subset.columns)
X = np.array(continuous_subset).astype('float64')
y = np.array(df['TotalQ'])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)
# knn = KNeighborsClassifier(n_neighbors=21)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# acc = metrics.accuracy_score(y_test, y_pred)
# print(acc)
# print(X_train)
# ---
clf = SVC(C=0.8, kernel='rbf', gamma=1, decision_function_shape='ovo')
clf.fit(X_train, y_train.ravel())
print(clf.score(X_train, y_train))
y_hat = clf.predict(X_train)

count = 0
for i in range(len(X_train)):
    if y_hat[i] != y_train[i]:
        count += 1
        print("%d/%d" % (count,len(X_train)))

# ---



