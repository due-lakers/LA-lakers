from flask import Flask, request
from flask_cors import CORS
import pickle
import pandas as pd
import datetime
import json
import numpy as np
import math
from labelEncoder import encode
from flask_restful import Resource, Api
import util.MongoDb as M

app = Flask(__name__)
app.debug = True
CORS(app, supports_credentials=True)
api = Api(app)
db = 'lakers'
col = 'predict'
inputs = [
    'gender',
    'NationalITy',
    'PlaceofBirth',
    'StageID',
    'GradeID',
    'SectionID',
    'Topic',
    'Semester',
    'raisedhands',
    'VisITedResources',
    'AnnouncementsView',
    'Discussion',
    'StudentAbsenceDays'
]

df = pd.read_csv('data/data.csv')
gender = {}
topic = {}
numD = {}
national = {}
f_spliter = range(0, 100, 20)


class GetGenderData(Resource):
    @staticmethod
    def get():
        gender_counter = df['gender'].value_counts()
        gender['data'] = [{'value': str(gender_counter.values[i]), 'name': item} for i, item in
                          enumerate(gender_counter.index.values)]
        return gender


class GetTopicData(Resource):
    @staticmethod
    def get():
        topic_counter = df['Topic'].value_counts()
        topic = {"name": topic_counter.index.values.tolist(), "value": topic_counter.values.tolist()}
        return topic


class GetNationalData(Resource):
    @staticmethod
    def get():
        national_counter = df['NationalITy'].value_counts()
        national['data'] = [{'value': str(national_counter.values[i]), 'name': item} for i, item in
                            enumerate(national_counter.index.values)]
        return national


class GetRecentNums(Resource):
    @staticmethod
    def get():
        return M.getRecentNums(db,col)


class GetNumData(Resource):
    @staticmethod
    def get():
        # raisedhands_spliter = pd.cut((df.where(df['Class'] == 'H')['raisedhands'], spliter)).value_counts()
        # VisITedResources_spliter = pd.cut((df.where(df['Class'] == 'H')['VisITedResources'], spliter)).value_counts()
        # AnnouncementsView_spliter = pd.cut((df.where(df['Class'] == 'H')['AnnouncementsView'], spliter)).value_counts()
        # Discussion_spliter = pd.cut((df.where(df['Class'] == 'H')['Discussion'], spliter)).value_counts()

        cl = [df.where(df['Class'] == 'L')['Class'].value_counts().agg('sum'),
              df.where(df['Class'] == 'M')['Class'].value_counts().agg('sum'),
              df.where(df['Class'] == 'H')['Class'].value_counts().agg('sum'),
              ]

        raisedhands = [df.where(df['Class'] == 'L')['raisedhands'].agg('mean'),
                       df.where(df['Class'] == 'M')['raisedhands'].agg('mean'),
                       df.where(df['Class'] == 'H')['raisedhands'].agg('mean')]

        VisITedResources = [df.where(df['Class'] == 'L')['VisITedResources'].agg('mean'),
                            df.where(df['Class'] == 'M')['VisITedResources'].agg('mean'),
                            df.where(df['Class'] == 'H')['VisITedResources'].agg('mean')]

        Discussion = [df.where(df['Class'] == 'L')['Discussion'].agg('mean'),
                      df.where(df['Class'] == 'M')['Discussion'].agg('mean'),
                      df.where(df['Class'] == 'H')['Discussion'].agg('mean')]

        AnnouncementsView = [df.where(df['Class'] == 'L')['AnnouncementsView'].agg('mean'),
                             df.where(df['Class'] == 'M')['AnnouncementsView'].agg('mean'),
                             df.where(df['Class'] == 'H')['AnnouncementsView'].agg('mean')]

        StudentAbsenceDays = [df.where(df['Class'] == 'L')['StudentAbsenceDays'].value_counts()['Above-7'],
                              df.where(df['Class'] == 'M')['StudentAbsenceDays'].value_counts()['Above-7'],
                              df.where(df['Class'] == 'H')['StudentAbsenceDays'].value_counts()['Above-7']]

        numD = {
            "label": ['raisedhands', 'VisITedResources', 'Discussion', 'AnnouncementsView'],
            "xData": {
                "raisedhands": [math.ceil(i) for i in raisedhands],
                "VisITedResources": [math.ceil(i) for i in VisITedResources],
                "Discussion": [math.ceil(i) for i in Discussion],
                "AnnouncementsView": [math.ceil(i) for i in AnnouncementsView],
                "StudentAbsenceDays": [math.ceil(i) for i in StudentAbsenceDays]
            },
            "yData": ['L', 'M', 'H']
        }
        return numD


class Predict(Resource):
    @staticmethod
    def post():
        result = request.json
        print(result)
        c = pd.DataFrame(result, index=[0])
        inputs[0] = encode(result['gender'])
        inputs[1] = encode(result['NationalITy'])
        inputs[2] = encode(result['PlaceofBirth'])
        inputs[3] = encode(result['StageID'])
        inputs[4] = encode(result['GradeID'])
        inputs[5] = encode(result['SectionID'])
        inputs[6] = encode(result['Topic'])
        inputs[7] = encode('FS' if result['Semester'] == 'F' else 'S')
        inputs[8] = result['raisedhands']
        inputs[9] = result['VisITedResources']
        inputs[10] = result['AnnouncementsView']
        inputs[11] = result['Discussion']
        inputs[12] = encode(result['StudentAbsenceDays'])
        print('form', inputs)
        data = {}
        if inputs.__contains__(None):
            data['code'] = 1
            data['data'] = 'bad input, please check your input!'
            return json.dumps(data, sort_keys=False)
        f = open('model/svm.model13', 'rb')
        with open('model/svm.model13', 'rb') as f:
            svm_clf, label_encoder, sorted_named_scores = pickle.load(f)
        r = svm_clf.predict(np.array(inputs).reshape(1, -1))
        it = label_encoder.inverse_transform(r)
        predict_result = it.tolist()[0]

        result['result'] = predict_result
        result['createTime'] = datetime.datetime.now()
        # get the results that the same as the predictor
        M.insert(col, result)
        all = M.getAll(db, col)
        rs = [
            1 - M.getResult('L') / all,
            1 - M.getResult('M') / all,
            1 - M.getResult('H') / all
        ]
        rs.sort()
        rate = 1 - M.getResult(predict_result) / all
        print('M.getResult(predict_result)', M.getResult(predict_result))
        print('M.getResult(predict_result)', M.getAll(db, col))

        data['code'] = 200
        data['data'] = {
            'result': predict_result,
            'eigen': sorted_named_scores,
            'rs': rs,
            'rate': str(rate),
            'rStudents': str(M.getResult(predict_result))
        }
        print(result)
        print(sorted_named_scores)
        print(json.dumps(data, sort_keys=False))
        return json.dumps(data, sort_keys=False)


api.add_resource(Predict, '/predict')
api.add_resource(GetGenderData, '/get_gender_data')
api.add_resource(GetNationalData, '/get_national_data')
api.add_resource(GetTopicData, '/get_topic_data')
api.add_resource(GetNumData, '/get_num_data')
api.add_resource(GetRecentNums, '/get_recent_nums')

if __name__ == '__main__':
    app.run()
