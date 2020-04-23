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

@app.route('/club/Premier-League', methods=['GET', 'OPTIONS']) # get data of a particular record id
# @auth.login_required
def getData():
	sql_cmd = "SELECT * FROM Clubs WHERE Club_name={}".format("Premier League")
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	for entries in data:
		print(entries)
		result = {
			'id': int(entries[0]),
			'description': entries[1],
			'expenditure': int(entries[2]),
			'category': entries[3],
			'date': str(entries[4])
		}
	return jsonify(result) 