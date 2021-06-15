from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import sklearn
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open('model.pkl',"rb")
model=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Hi, Welcome!!"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    """
    Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted values is " + str(prediction)






if __name__=='__main__':
    app.run()