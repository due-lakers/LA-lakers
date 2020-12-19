import json
from flask import Flask, render_template, request, url_for
import numpy as np

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return render_template('index.html', title='Machine Learning')


if __name__ == '__main__':
    app.run()
