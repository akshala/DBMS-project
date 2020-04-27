from flask import Flask, render_template, jsonify, abort, make_response,request,redirect
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
	# passwd="",
	database="football"
)

mycursor = mydb.cursor()

@app.route("/",methods = ['POST', 'GET', 'OPTIONS'])
def getPage_index():
	if request.method == "POST":
		uname = request.form["uname"]
		password = request.form["pwd"]
		print("yes")
		print(uname,password)
		if (uname == "player" and password == "Player@123"):
			return redirect(url_for('getData_player'))
		elif (uname == "manager" and password == "Manager@123"):
			return redirect(url_for("getData_manager"))
		elif (uname == "league" and password == "League@123"):
			return redirect(url_for("getData_club"))
		elif (uname == "referee" and password == "Referee@123"):
			return redirect(url_for("getData_referee"))
		elif (uname == "Arsenal" and password == "Arsenal@123"):
			return redirect(url_for("get_club_after_login", club=uname))
	print("fkn hell")
	return render_template('index.html', r=[])

@app.route("/contact_us")
def getPage_contact_us():
    return render_template('contact.html')

@app.route("/club_after_login")
def get_club_after_login():
	club = request.args['club']
	sql_cmd = "SELECT * from Player where Club=\'{}\'".format(club)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print("data", data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Player_ID': int(entries[0]),
			'Name': str(entries[1]),
			'Games_Played': int(entries[2]),
			'Goals': int(entries[3]),
			'Assists': int(entries[4]),
			'GoalsConceded': int(entries[5]),
			'CleanSheets': int(entries[6]),
			'Position': str(entries[7]),
			'Age': int(entries[8]),
			'Contract': str(entries[9]),
			'MarketValue': float(entries[10]),
			'Height': float(entries[11]),
			'Club': str(entries[13]),
		})
	print(result, flush=True)
	return render_template('afterLogin_club.html', club=club, r=result)


@app.route("/club_after_player_deletion")
def delete_player():
	Player_ID =  request.args['Player_ID']
	current_club = request.args['Club']
	sql_cmd = "UPDATE Player set Club=\'{}\' where Player_ID={}".format("-", Player_ID)
	mycursor.execute(sql_cmd)
	mydb.commit()
	return redirect(url_for("get_club_after_login", club=current_club))


@app.route("/refereeData", methods=['POST', 'GET'])
def getData_referee():
	if request.method == 'POST':
		League = request.form['League']
		Yellow_cards = request.form['Yellow_cards']
		Red_cards = request.form['Red_cards']
		Penalties_given = request.form['Penalties_given']

		if(League == 'None'):
			sql_cmd = "SELECT * from Referee where Yellow_cards>={} and Red_cards>={} and Penalties_given>={}".format(Yellow_cards, Red_cards, Penalties_given) 
		else:
			sql_cmd = "SELECT * from Referee where League_name=\'{}\' and Yellow_cards>={} and Red_cards>={} and Penalties_given>={}".format(League, Yellow_cards, Red_cards, Penalties_given) 
		mycursor.execute(sql_cmd)
		data = mycursor.fetchall() # data comes in the form of a list 
		print("data", data, flush=True)
		result = []
		for entries in data:
			result.append({
				'Referee_id': int(entries[0]),
				'Referee_name': str(entries[1]),
				'League_name': str(entries[2]),
				'Yellow_cards': int(entries[3]),
				'Red_cards': int(entries[4]),
				'Penalties_given': int(entries[5]),
			})
		print(result, flush=True)
		return render_template('player_referee.html', r=result)
	return render_template("player_referee.html",r = [])

@app.route("/clubData", methods=['POST', 'GET'])
def getData_club():
	if request.method == 'POST':
		League = request.form['League']

		if(League == 'None'):
			sql_cmd = "SELECT c.Club_name, m.Name, c.League_name, c.Stadium from Club as c, Manager as m where (m.Manager_ID = c.Manager_ID)"
		else:
			sql_cmd = "SELECT c.Club_name, m.Name, c.League_name, c.Stadium from Club as c, Manager as m where (m.Manager_ID = c.Manager_ID) and c.League_name=\'{}\'".format(League)
		mycursor.execute(sql_cmd)
		data = mycursor.fetchall() # data comes in the form of a list 
		print("data", data, flush=True)
		result = []
		for entries in data:
			result.append({
				'Club_name': str(entries[0]),
				'Manager_name': str(entries[1]),
				'League_name': str(entries[2]),
				'Stadium': str(entries[3]),
			})
		print(result, flush=True)
		return render_template('player_club.html', r=result)
	return render_template("player_club.html",r = [])

@app.route("/managerData", methods=['POST', 'GET'])
def getData_manager():
	if request.method == 'POST':
		Club = str(request.form['Club'])
		Age = int(request.form['Age'])
		Formation = str(request.form['Formation'])
		win = float(request.form["Win Percentage"])
		flag = False
		if (Club=="None" and Formation=="None"):
			sql_cmd = "SELECT * from Manager where Age>={} and Win_Percentage>={}".format(Age, win)
		elif (Club == "None"):
			sql_cmd = "SELECT * from Manager where Formation=\'{}\' and Age>={} and Win_Percentage>={}".format(Formation,Age, win)
		elif (Formation == "None"):
			sql_cmd = "select * from Manager as M where M.Manager_ID in (select C1.Manager_ID from Club as C1 where C1.Club_name =\'{}\' and C1.Manager_ID =M.Manager_ID);".format(Club)
			flag = True
		else:
			sql_cmd = "select * from Manager as M where M.Manager_ID in (select C1.Manager_ID from Club as C1 where C1.Club_name =\'{}\' and C1.Manager_ID =M.Manager_ID);".format(Club)
			flag = True
		print(sql_cmd)
		mycursor.execute(sql_cmd)
		data = mycursor.fetchall() # data comes in the form of a list 
		# print("data", data, flush=True)
		result = []
		for entries in data:
			result.append({
				'Manager_ID': int(entries[0]),
				'Name': str(entries[1]),
				'Age': str(entries[2]),
				'Country': str(entries[3]),
				'Formation': str(entries[4]),
				'Contract': str(entries[5]),
				'WinPercentage': int(entries[6]),
			})
		if (flag):
			ans = result[0]
			if (Formation !="None"):
				age = int(ans["Age"])
				Win = float(ans["WinPercentage"])
				forms = str(ans["Formation"])
				if (age>= Age and Win>=win and forms == Formation):
					pass
				else:
					result = []
			else:
				age = int(ans["Age"])
				Win = float(ans["WinPercentage"])

				if (age>= Age and Win>=win):
					pass
				else:
					print("OH NO")
					result = []

		print("ANS: ",result)
		return render_template("player_manager.html",r=result)	
	return render_template("player_manager.html",r=[])

@app.route("/player_data", methods=['POST', 'GET'])
def getData_player():
	if request.method == 'POST':
		Position = request.form['Position']
		Club = request.form['Club']
		Games_Played = request.form['Games_Played']
		Goals = request.form['Goals']
		Assists = request.form['Assists']
		GoalsConceded = request.form['GoalsConceded']
		CleanSheets = request.form['CleanSheets']
		Age = request.form['Age']
		MarketValue = request.form['MarketValue']
		Height = request.form['Height']

		print(Position, Club, flush=True)
		if(Position == 'None' and Club == 'None'):
			sql_cmd = "SELECT * from Player where Games_Played>={} and Goals>={} and Assists>={} and GoalsConceded>={} and CleanSheets>={} and Age>={} and MarketValue>={} and Height>={}".format(Games_Played, Goals, Assists, GoalsConceded, CleanSheets, Age, MarketValue, Height)
		elif(Position == 'None' and Club != 'None'):
			sql_cmd = "SELECT * from Player where Club=\'{}\' and Games_Played>={} and Goals>={} and Assists>={} and GoalsConceded>={} and CleanSheets>={} and Age>={} and MarketValue>={} and Height>={}".format(Club, Games_Played, Goals, Assists, GoalsConceded, CleanSheets, Age, MarketValue, Height)
		elif(Position != 'None' and Club == 'None'):
			sql_cmd = "SELECT * from Player where Position=\'{}\' and Games_Played>={} and Goals>={} and Assists>={} and GoalsConceded>={} and CleanSheets>={} and Age>={} and MarketValue>={} and Height>={}".format(Position, Games_Played, Goals, Assists, GoalsConceded, CleanSheets, Age, MarketValue, Height)
		else:
			sql_cmd = "SELECT * from Player where Position=\'{}\' and Club=\'{}\' and Games_Played>={} and Goals>={} and Assists>={} and GoalsConceded>={} and CleanSheets>={} and Age>={} and MarketValue>={} and Height>={}".format(Position, Club, Games_Played, Goals, Assists, GoalsConceded, CleanSheets, Age, MarketValue, Height)
		print(sql_cmd)
		mycursor.execute(sql_cmd)
		data = mycursor.fetchall() # data comes in the form of a list 
		print("data", data, flush=True)
		result = []
		for entries in data:
			result.append({
				'Player_ID': int(entries[0]),
				'Name': str(entries[1]),
				'Games_Played': int(entries[2]),
				'Goals': int(entries[3]),
				'Assists': int(entries[4]),
				'GoalsConceded': int(entries[5]),
				'CleanSheets': int(entries[6]),
				'Position': str(entries[7]),
				'Age': int(entries[8]),
				'Contract': str(entries[9]),
				'MarketValue': float(entries[10]),
				'Height': float(entries[11]),
				'Club': str(entries[13]),
			})
		print(result, flush=True)
		return render_template('player.html', r=result)
	return render_template("player.html",r = [])

@app.route('/club/Premier-League', methods=['GET', 'OPTIONS'])
def getData_club_Premier_League():
	sql_cmd = "SELECT C.Club_name, M.Name, C.Stadium from Manager as M , Club as C where M.Manager_Id in (select M1.Manager_ID from Manager as M1 where M1.Manager_ID = C.Manager_ID) and League_name=\'{}\'".format("Premier League")
	# print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Club_name': str(entries[0]),
			'Manager_name': str(entries[1]),
			'Stadium': str(entries[2]),
		})
	# print("json data:", data, flush=True)
	return render_template('club.html', r=result, league="Premier League")

@app.route('/club/Serie-A', methods=['GET', 'OPTIONS'])
def getData_club_Serie_A():
	# sql_cmd = "SELECT * FROM Club WHERE League_name=\'{}\'".format("Serie A")
	sql_cmd = "SELECT C.Club_name, M.Name, C.Stadium from Manager as M , Club as C where M.Manager_Id in (select M1.Manager_ID from Manager as M1 where M1.Manager_ID = C.Manager_ID) and League_name=\'{}\'".format("Serie A")
	# print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Club_name': str(entries[0]),
			'Manager_name': str(entries[1]),
			'Stadium': str(entries[2]),
		})
	# print("json data:", data, flush=True)
	return render_template('club.html', r=result, league="Serie A")

@app.route('/club/La-Liga', methods=['GET', 'OPTIONS'])
def getData_club_La_Liga():
	sql_cmd = "SELECT C.Club_name, M.Name, C.Stadium from Manager as M , Club as C where M.Manager_Id in (select M1.Manager_ID from Manager as M1 where M1.Manager_ID = C.Manager_ID) and League_name=\'{}\'".format("La Liga")
	# print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Club_name': str(entries[0]),
			'Manager_name': str(entries[1]),
			'Stadium': str(entries[2]),
		})
	# print("json data:", data, flush=True)
	return render_template('club.html', r=result, league="La Liga")

@app.route('/results', methods=['GET', 'OPTIONS'])
def get_results():
	sql_cmd = "SELECT Home_team, Away_team, Date, Result from Match_Details where Date != '-:-' and Date != 'ppd.'"
	# print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Home_team': str(entries[0]),
			'Away_team': str(entries[1]),
			'Result': str(entries[2]),
			'Date': str(entries[3])
		})
	# print("json data:", data, flush=True)
	return render_template('result.html', r=result)

@app.route('/upcoming_matches', methods=['GET', 'OPTIONS'])
def get_upcoming_matches():
	sql_cmd = "SELECT Home_team, Away_team, Result from Match_Details where Date = '-:-'"
	# print(sql_cmd, flush=True)
	mycursor.execute(sql_cmd)
	data = mycursor.fetchall() # data comes in the form of a list 
	print(data, flush=True)
	result = []
	for entries in data:
		result.append({
			'Home_team': str(entries[0]),
			'Away_team': str(entries[1]),
			'Date': str(entries[2]),
		})
	# result = result[:13]
	# print("json data:", data, flush=True)
	return render_template('upcoming_matches.html', r=result)

@app.route('/awards', methods=['GET', 'OPTIONS'])
def get_awards():
	return render_template('awards.html')

if __name__ == "__main__":
    app.run(debug = True)