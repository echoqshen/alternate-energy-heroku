from flask import Flask
from flask import jsonify
import pandas as pd
import random
import os
from random import randrange
from pymongo import MongoClient
app = Flask(__name__)

@app.route("/mongo_data")
if __name__ == '__main__':
def mongo_data():

    client = MongoClient("")
    db = client.project1
    collection = db.project1
    query_mongo_df  = pd.DataFrame(list(collection.find()))
    first_20 = query_mongo_df.head(20)
    return first_20.to_html()

@app.route("/pass")
def passes():
    my_pass = os.environ['pass']
    msg = "pass: " + my_pass
    return msg

@app.route("/vars")
def vars():
    my_vars = os.environ
    my_vars_dict = dict(my_vars)
    return jsonify(my_vars_dict)

if __name__ == '__main__':
    app.run()
