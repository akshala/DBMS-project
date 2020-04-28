import mysql.connector
import mysql

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Akshala@12",
	# passwd="",
	database="football"
)

mycursor = mydb.cursor()

cmnd = "select S.Player_ID, Goals,Assists from Season_player as S where S.Player_ID in (select P.Player_ID from Player as P where P.Position='Goalkeeper' and S.Player_ID = P.Player_ID)"

mycursor.execute(cmnd)
data = mycursor.fetchall()
# print(data)

s = []
for i in range(len(data)):
    s.append([int(data[i][0]),int(data[i][1]),int(data[i][2])])

cmnd = "update Season_player set GoalsConceded=24, CleanSheets=10 where Player_ID =1"
mycursor.execute(cmnd)
for i in data:
    id = i[0]
    c = i[1]
    s = i[2]
    # print(c,s)
    cmnd = "update Season_player set GoalsConceded={}, CleanSheets={} where Player_ID={}".format(c,s,id)
    mycursor.execute(cmnd)
    mydb.commit()
    print(mycursor.rowcount)


# print(s)