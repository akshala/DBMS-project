from flask import Flask, render_template, jsonify, abort, make_response
from flask import request, url_for
from flask import request, current_app
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import mysql.connector
import mysql
import json
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__, static_folder='/home/akshala/Documents/IIITD/fourthSem/DBMS/Project/flask/specer/football_flask/static', template_folder='/home/akshala/Documents/IIITD/fourthSem/DBMS/Project/flask/specer/football_flask')

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Akshala@12",
	database="football"
)

mycursor = mydb.cursor()

@app.route("/")
def getPage():
    return render_template('index.html')

@app.route('/club/Premier-League', methods=['GET', 'OPTIONS'])
def getData():
	sql_cmd = "SELECT * FROM Clubs WHERE Club_name={}".format("Premier League")
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	for entries in data:
		print(entries)
		result = {
			'Club_name': str(entries[0]),
			'Manager_ID': int(entries[1]),
			'League_name': str(entries[2]),
			'Stadium': str(entries[3]),
		}
	return jsonify(result)

if __name__ == "__main__":
    app.run()