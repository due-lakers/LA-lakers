import json
from flask import Flask, render_template, request, url_for
import pickle
import numpy as np

app = Flask(__name__, static_folder='./static')
app.debug = True


@app.route('/')
def hello_world():
    f2 = open('model/svm.model', 'rb')
    s2 = f2.read()
    l1 = [10., 17., 12., 40., 1., 1.]  # H
    l2 = [70., 82., 3., 73., 0., 0.]  # M
    l3 = [30., 52., 23., 33., 0., 1.]  # M

    # model1 = pickle.loads(s2)
    # expected = test_y
    # predicted = model1.predict(np.array(l1).reshape(1, -1))
    # return str(predicted)
    return render_template('index.html')


@app.route('/index')
def student():
    return render_template('index.html')


@app.route('/form')
def formPage():
    return render_template('form_controls.html', title='Machine Learning')


# @app.route('/formTest',methods=['POST', 'GET'])
# def form():
#     if request.method=='POST':
#         print(request.form.get("test1"))
#         re=request.form.get("test1")
#
#
#
#     return render_template('form_controls.html', title='Machine Learning',results=re)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template("form_controls.html", result=result)


if __name__ == '__main__':
    app.run()
