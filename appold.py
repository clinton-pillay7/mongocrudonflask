from flask import Flask
import pymongo
from pymongo import MongoClient


app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://192.168.8.108:27017/cruddb

mongo = PyMongo(app)

if mongo == True:
	return "connected"

@app.route("/")
def home():
    return "Hello"




if __name__ == "__main__":
    app.run(debug=True)


