from flask import Flask
import socket
import pymongo


app = Flask(__name__)

#myclient = pymongo.MongoClient("mongodb://192.168.8.108:27017/")
myclient = pymongo.MongoClient("mongodb://root:rootpassword@192.168.8.108:27017/?authMechanism=DEFAULT")

dblist = []
for db in myclient.list_databases():
	dblist.append(db)

@app.route("/")
def home():
#        return f"Container ID: {socket.gethostname()}"
	 return dblist

if __name__ == "__main__":
	app.run(debug=True)


