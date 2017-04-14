# coding : utf-8

from flask import Flask, redirect, url_for, request
import numpy as np

class Api():

    def __init__(self, model):
        self.model = model
        self.app = Flask(__name__)

        @self.app.route('/predict/<model>/<data>')
        def predict(model, data):
            # transformation des données en np.array
            print(type(data))
            x = np.fromstring(data, dtype = int, sep = ' ')
            x = x.reshape(1, -1)
            print(x)
            print(type(x))
            # return "coucou"
            return np.array_str(self.model.predict(x))

        @self.app.route('/data',methods = ['POST', 'GET'])
        def data():
            data = request.form['data'] # il faut que ça soit un json
            return redirect(url_for('predict',data = data, model = self.model))
