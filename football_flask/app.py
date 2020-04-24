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
from pprint import pprint

app = Flask(__name__, static_folder='./static', template_folder='.')

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Akshala@12",
	database="football"
)

mycursor = mydb.cursor()

@app.route("/")
def getPage_index():
    return render_template('index.html')

@app.route("/contact_us")
def getPage_contact_us():
    return render_template('contact.html')

@app.route('/club/Premier-League', methods=['GET', 'OPTIONS'])
def getData_club_Premier_League():
	sql_cmd = "SELECT * FROM Club WHERE League_name=\'{}\'".format("Premier League")
	print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Club_name': str(entries[0]),
			'Manager_ID': int(entries[1]),
			'League_name': str(entries[2]),
			'Stadium': str(entries[3]),
		})
	data = json.dumps(result)
	print("json data:", data, flush=True)
	return render_template('club.html', r=data)

@app.route('/club/Serie-A', methods=['GET', 'OPTIONS'])
def getData_club_Serie_A():
	sql_cmd = "SELECT * FROM Club WHERE League_name=\'{}\'".format("Serie A")
	print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Club_name': str(entries[0]),
			'Manager_ID': int(entries[1]),
			'League_name': str(entries[2]),
			'Stadium': str(entries[3]),
		})
	data = json.dumps(result)
	print("json data:", data, flush=True)
	return render_template('club.html', r=data)

@app.route('/club/La-Liga', methods=['GET', 'OPTIONS'])
def getData_club_La_Liga():
	sql_cmd = "SELECT * FROM Club WHERE League_name=\'{}\'".format("La Liga")
	print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Club_name': str(entries[0]),
			'Manager_ID': int(entries[1]),
			'League_name': str(entries[2]),
			'Stadium': str(entries[3]),
		})
	data = json.dumps(result)
	print("json data:", data, flush=True)
	return render_template('club.html', r=data)

if __name__ == "__main__":
    app.run(debug = True)