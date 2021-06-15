from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
pickle_in = open(model.plk,"rb")
model=pickle.load(pickle_in)




if __name__=='__main__':
    app.run()