import mysql.connector

dbase,table = input().split() #first line of input: the database and the table you want to insert to SPACE SEPARATED
params = input().split() #second line of input: the paramaters you want to add to the table SPACE SEPARATED
values = input().split(",") #third line of input: values of the params COMMA SEPARATED (DONT USE SPACE BEFORE AND AFTER COMMA)

#preprocessing
paramString = ""
tupleValue = tuple(values)
stringFormatters = ""

for i in range(len(params)):
    if (i ==len(params)-1):
        paramString += params[i]
        stringFormatters += "%s"
    else:
        paramString += params[i]+ ", "
        stringFormatters += "%s, "

#database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="psswd",
  database=dbase
)
mycursor = mydb.cursor()

#actual insertion to table
sql = "INSERT INTO "+ table+ "("+ paramString+")"+ "VALUES "+"("+stringFormatters+")"
mycursor.execute(sql, tupleValue)

mydb.commit()

print(mycursor.rowcount, "record inserted.")