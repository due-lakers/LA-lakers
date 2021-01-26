from flask import jsonify, Flask, request
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
from labelEncoder import encode
from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True
CORS(app, supports_credentials=True)
api = Api(app)

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


class Predict(Resource):

    def post(self):
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
        inputs[7] = encode('FS' if result['Semester'] == 'F' else'S')
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
            return jsonify(data)
        f = open('model/svm.model13', 'rb')
        with open('model/svm.model13', 'rb') as f:
            svm_clf, label_encoder = pickle.load(f)

        r = svm_clf.predict(np.array(inputs).reshape(1, -1))
        it = label_encoder.inverse_transform(r)
        data['code'] = 200
        data['data'] = it.tolist()[0]
        return jsonify(data)


api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run()
