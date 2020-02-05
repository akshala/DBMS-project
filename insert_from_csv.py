import mysql.connector
import csv

dbase,table = input().split() #first line of input: the database and the table you want to insert to SPACE SEPARATED
source = input() # path to csv
# params = input().split() #second line of input: the paramaters you want to add to the table SPACE SEPARATED
# values = input().split(",") #third line of input: values of the params COMMA SEPARATED (DONT USE SPACE BEFORE AND AFTER COMMA)

#preprocessing
paramString = ""
stringFormatters = ""
params =''
values = ''

line = 0
with open(source) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    if line == 0:
      params += (' '.join(row))
    else:
      values += (' '.join(row))
tupleValue = tuple(values)

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
  user="dbms",
  passwd="12345678",
  database=dbase
)
mycursor = mydb.cursor()

#actual insertion to table
sql = "INSERT INTO "+ table+ "("+ paramString+")"+ "VALUES "+"("+stringFormatters+")"
mycursor.execute(sql, tupleValue)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
