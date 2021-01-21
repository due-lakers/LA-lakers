import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import pickle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# df = pd.read_csv('data\data.csv',engine='python',sep=',')
# df.head()
# df['Score'] = df['Class']
# df['Score'].loc[df.Score == 'Low-Level'] = 0.0
# df['Score'].loc[df.Score == 'Middle-Level'] = 1.0
# df['Score'].loc[df.Score == 'High-Level'] = 2.0
# continuous_subset = df.iloc[:, 9:13]
#
# continuous_subset['gender'] = np.where(df['gender'] == 'M', 1, 0)
# continuous_subset['Parent'] = np.where(df['Relation'] == 'Father', 1, 0)
# # print(continuous_subset)
# X = np.array(continuous_subset).astype('float64')
# y = np.array(df['Score'])
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=1)

train_data = pd.read_csv("data/data.csv")
train_Y = train_data["Class"]
train_X = train_data.drop(columns=['NationalITy','ParentschoolSatisfaction','StudentAbsenceDays','Class','GradeID','SectionID','Topic','Relation','Semester','StageID','PlaceofBirth'])
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
    # df.NationalITy = NationEncoder.fit_transform(df.NationalITy)
    # df.PlaceofBirth = BirthEncoder.fit_transform(df.PlaceofBirth)
    # df.StageID = StagedEncoder.fit_transform(df.StageID)
    # df.GradeID = GradeEncoder.fit_transform(df.GradeID)
    # df.SectionID = SemesterEncoder.fit_transform(df.SectionID)
    # df.Topic  = TopicsEncoder.fit_transform(df.Topic)
    # df.Semester = SemesterEncoder.fit_transform(df.Semester)
    # df.Relation = RelationEncoder.fit_transform(df.Relation)
    df.ParentAnsweringSurvey  = ParentschoolSatisfactionEncoder.fit_transform(df.ParentAnsweringSurvey)
    # df.ParentschoolSatisfaction = ParentschoolSatisfactionEncoder.fit_transform(df.ParentschoolSatisfaction)
    # df.StudentAbsenceDays = StagedEncoder.fit_transform(df.StudentAbsenceDays)
    return df

train_X = cope_X(train_X).values
labelEncoder = LabelEncoder()
train_Y = labelEncoder.fit_transform(train_Y)
X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=.3, random_state=0)

# knn = KNeighborsClassifier(n_neighbors=21)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# acc = metrics.accuracy_score(y_test, y_pred)
# print(acc)
# print(X_train)
# ---
# clf = SVC(C=1, kernel='rbf')
# # clf = SVC(kernel='rbf', C=1).fit(X_train, y_train)
#
# scores = cross_val_score(clf, X_train, y_train, cv=5, scoring='accuracy')
#
# print('cross_val_score:',scores.mean())
# print(clf.score(X_train, y_train))
# y_hat = clf.predict(X_train)
krange = range(1,55)
ks = []
bs = []
for l in krange:
    clf = SVC(C=1+l*0.4, kernel='rbf').fit(X_train, y_train)
    scores = cross_val_score(clf,X_train,y_train,cv=5,scoring='accuracy')
    ks.append(scores.mean())
    bs.append(clf.score(X_train,y_train))
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
count = 0
clf = SVC(C=13, kernel='rbf').fit(X_train, y_train)
print(clf.score(X_train, y_train))
y_hat = clf.predict(X_train)

# for i in range(len(X_train)):
#     # print(y_hat[i])
#     # print(X_train[i])
#     if y_hat[i] != y_train[i]:
#         count += 1
#         print(y_train[i])
#         print("%d/%d" % (count,len(X_train)))

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
