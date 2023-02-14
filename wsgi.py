from flask import Flask
import socket
import pymongo
import json
from flask import request
import os
from flask import json
from flask import jsonify


app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://root:rootpassword@192.168.8.108:27017/?authMechanism=DEFAULT")

mydb = myclient.cruddb

mycol = mydb.crudcollection

@app.route("/")
def home():
#    return f"Container ID: {socket.gethostname()}"
	documents = mycol.find()
	response = []
	for document in documents:
		document["_id"] = str(document["_id"])
		response.append(document)
	return jsonify(response)

@app.route("/api")
def api():
	#return f"Container ID: {socket.gethostname()}"
	#gender = request.args.get('gendervar')
	documents = mycol.find({"gender":"Female"})
	response = []
	for document in documents:
		document["_id"] = str(document["_id"])
		response.append(document)
	return jsonify(response)



if __name__ == "__main__":
	app.run(debug=True)

