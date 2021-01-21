import json
from flask import Flask, render_template, request, url_for
import pickle
import numpy as np

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    f2 = open('model/svm.model', 'rb')
    s2 = f2.read()
    l1 = [10., 17., 12., 40., 1., 1.] # H
    l2 = [70., 82., 3., 73., 0. ,0.] #M
    l3 = [30., 52., 23., 33., 0., 1.] #M

    model1 = pickle.loads(s2)
    # expected = test_y
    predicted = model1.predict(np.array(l1).reshape(1,-1))
    return str(predicted)

@app.route('/login')
def login():
    return render_template('index.html', title='Machine Learning')


if __name__ == '__main__':
    app.run()
