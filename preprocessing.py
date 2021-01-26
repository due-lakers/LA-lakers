import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import pickle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,LabelBinarizer
train_data = pd.read_csv("data\data.csv")

str = {'VisITedResources': '0', 'raisedhands': '88', 'gender': 'M', 'AnnouncementsView': '88', 'Discussion': '88', 'Topic': 'IT', 'Semester': 'F', 'StageID': 'lowerlevel', 'SectionID': 'A', 'NationalITy': 'KW', 'GradeID': 'G-04', 'PlaceofBirth': 'KuwaIT', 'StudentAbsenceDays': 'Under-7'}

train_Y = train_data["Class"]
train_X = train_data.drop(columns=['ParentAnsweringSurvey','ParentschoolSatisfaction','Relation','Class'])
#
# continuous_subset['gender'] = np.where(df['gender'] == 'M', 1, 0)
# continuous_subset['Parent'] = np.where(df['Relation'] == 'Father', 1, 0)
# print(continuous_subset)
# X = np.array(continuous_subset).astype('float64')
# sub['gender'] = np.where(df['gender'] == 'M', 1, 0)
# sub['Parent'] = np.where(df['Relation'] == 'Father', 1, 0)
# X = np.array(sub).astype('float64')
#
# y = np.array(df['Class'])
krange = range(1,10)

print("cac",train_X.values)

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
    df.Topic  = TopicsEncoder.fit_transform(df.Topic)
    print(TopicsEncoder.classes_)
    df.Semester = SemesterEncoder.fit_transform(df.Semester)
    print(SemesterEncoder.classes_)

    # df.Relation = RelationEncoder.fit_transform(df.Relation)
    # df.ParentAnsweringSurvey  = ParentschoolSatisfactionEncoder.fit_transform(df.ParentAnsweringSurvey)
    # df.ParentschoolSatisfaction = ParentschoolSatisfactionEncoder.fit_transform(df.ParentschoolSatisfaction)
    df.StudentAbsenceDays = StudentAbsenceDaysEncoder.fit_transform(df.StudentAbsenceDays)
    print(StagedEncoder.classes_)

    # with open('model/encoder', 'wb+') as f:
    #   pickle.dump((genderEncoder,NationEncoder,BirthEncoder,StagedEncoder,GradeEncoder,TopicsEncoder,SemesterEncoder), f, pickle.HIGHEST_PROTOCOL) # uid, iid
    return df
train_X = cope_X(train_X).values



label_encoder = LabelEncoder()
print('label_encoder',label_encoder)
train_Y = label_encoder.fit_transform(train_Y)
X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y, test_size=.2, random_state=7)

svm_clf = SVC(kernel='linear').fit(X_train, y_train)
print("svm 分类器：",svm_clf.score(X_test, y_test))
ks = []
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
# print(confusion_matrix(y_train, y_hat))
# print(classification_report(y_train, y_hat))
# ---


# with open('model/svm.model13', 'wb+') as f:
#   pickle.dump((svm_clf,label_encoder), f, pickle.HIGHEST_PROTOCOL) # uid, iid
# # s=pickle.dumps(svm_clf)
# # f=open('model/svm.model13', "wb+")
# # f.write(s)
# # f.close()
# print ("Done\n")
#
#

c = pd.DataFrame(str, index=[1])
print(c.values)
label_encoder.fit(c.values[0])
aa = label_encoder.transform(c.values[0])
print('aa',aa)
print(label_encoder.classes_)
with open('model/svm.model13', 'rb') as f:
    svm_clf, label_encoder = pickle.load(f)
with open('model/encoder', 'rb') as f:
    genderEncoder, NationEncoder, BirthEncoder, StagedEncoder, GradeEncoder, TopicsEncoder, SemesterEncoder = pickle.load(f)
c.gender = genderEncoder.fit_transform(c.gender)
c.NationalITy = NationEncoder.fit_transform(c.NationalITy)
c.PlaceofBirth = BirthEncoder.fit_transform(c.PlaceofBirth)
c.StageID = StagedEncoder.fit_transform(c.StageID)
c.GradeID = GradeEncoder.fit_transform(c.GradeID)
c.SectionID = SemesterEncoder.fit_transform(c.SectionID)
c.Topic  = TopicsEncoder.fit_transform(c.Topic)
c.Semester = SemesterEncoder.fit_transform(c.Semester)
c.StudentAbsenceDays = StagedEncoder.fit_transform(c.StudentAbsenceDays)
r = svm_clf.predict(X_test)
print('c', c.values)
# d = cope_X(c).values
# print(d)
cc = [i for i in aa]
print('cc',np.array(cc))
r = svm_clf.predict(np.array(cc).reshape(1,-1))
it = label_encoder.inverse_transform(r)
print(it)
it = label_encoder.inverse_transform(r)
