import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder, LabelBinarizer

train_data = pd.read_csv("data\data.csv")
train_data['Semester'] = np.where(train_data['Semester'] == 'F', 'FS', 'S')
train_Y = train_data["Class"]
train_X = train_data.drop(columns=['ParentAnsweringSurvey', 'ParentschoolSatisfaction', 'Relation', 'Class'])
krange = range(1, 10)
names = train_X.columns


def cope_X(df):
    genderEncoder = LabelEncoder()
    NationEncoder = LabelEncoder()
    BirthEncoder = LabelEncoder()
    StagedEncoder = LabelEncoder()
    GradeEncoder = LabelEncoder()
    SectionsEncoder = LabelEncoder()
    TopicsEncoder = LabelEncoder()
    SemesterEncoder = LabelEncoder()
    StudentAbsenceDaysEncoder = LabelEncoder()
    df.gender = genderEncoder.fit_transform(df.gender)
    print(genderEncoder.classes_)
    df.NationalITy = NationEncoder.fit_transform(df.NationalITy)
    print(NationEncoder.classes_)
    df.PlaceofBirth = BirthEncoder.fit_transform(df.PlaceofBirth)
    print(BirthEncoder.classes_)
    df.StageID = StagedEncoder.fit_transform(df.StageID)
    print(StagedEncoder.classes_)
    df.GradeID = GradeEncoder.fit_transform(df.GradeID)
    print(GradeEncoder.classes_)
    df.SectionID = SectionsEncoder.fit_transform(df.SectionID)
    print(SectionsEncoder.classes_)
    df.Topic = TopicsEncoder.fit_transform(df.Topic)
    print(TopicsEncoder.classes_)
    df.Semester = SemesterEncoder.fit_transform(df.Semester)
    print(SemesterEncoder.classes_)
    df.StudentAbsenceDays = StudentAbsenceDaysEncoder.fit_transform(df.StudentAbsenceDays)
    print(StagedEncoder.classes_)
    # with open('model/encoder', 'wb+') as f:
    #   pickle.dump((genderEncoder,NationEncoder,BirthEncoder,StagedEncoder,GradeEncoder,TopicsEncoder,SemesterEncoder), f, pickle.HIGHEST_PROTOCOL) # uid, iid
    return df


train_X = cope_X(train_X).values
label_encoder = LabelEncoder()
print('label_encoder', label_encoder)
train_Y = label_encoder.fit_transform(train_Y)
X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=.2, random_state=7)
svm_clf = SVC(kernel='linear').fit(X_train, y_train)
X_new = SelectKBest(f_regression, k=5).fit(X_train, y_train)
scores = X_new.scores_
y_hat = svm_clf.predict(X_train)
named_scores = zip(names, scores)
sorted_named_scores = dict(sorted(named_scores, key=lambda z: z[1], reverse=True))
print("svm: ", svm_clf.score(X_test, y_test))
ks = []

# evaluation process
# for l in krange:
#     X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=0.2, random_state=l)
#     svm_clf = SVC(kernel='linear').fit(X_train, y_train)
#     y_hat = svm_clf.predict(X_train)
#     scores = cross_val_score(svm_clf,X_train,y_train,cv=10,scoring='accuracy')
#     ks.append(svm_clf.score(X_test, y_test))
# #
# plt.plot(krange,ks)
# plt.xlabel('Value')
# plt.ylabel('Cross-Validated Accuracy')
# plt.show()
# count = 0


# for i in range(len(X_train)):
#     # print(y_hat[i])
#     # print(X_train[i])
#     if y_hat[i] != y_train[i]:
#         count += 1
#
# print("%d/%d" % (count,len(X_train)))

# evaluate the algorithm
print(confusion_matrix(y_train, y_hat))
print(classification_report(y_train, y_hat))
# with open('model/svm.model13', 'wb+') as f:
#   pickle.dump((svm_clf,label_encoder,sorted_named_scores), f, pickle.HIGHEST_PROTOCOL) # uid, iid
# c = pd.DataFrame(str, index=[1])
# label_encoder.fit(c.values[0])