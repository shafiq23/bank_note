from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import sklearn

app=Flask(__name__)
pickle_in = open('model.pkl',"rb")
model=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Hi, Welcome!!"

@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted values is " + str(prediction)






if __name__=='__main__':
    app.run()