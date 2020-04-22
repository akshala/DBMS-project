import csv
import unicodedata

x = []
with open('club.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        first = unicodedata.normalize('NFD', row[0]).encode('ascii', 'ignore').decode("utf-8")  
        print(first) 
        second = unicodedata.normalize('NFD', row[1]).encode('ascii', 'ignore').decode("utf-8")   
        print(second) 
        third = unicodedata.normalize('NFD', row[2]).encode('ascii', 'ignore').decode("utf-8") 
        print(third)   
        fourth = unicodedata.normalize('NFD', row[3]).encode('ascii', 'ignore').decode("utf-8")   
        print(fourth)
        x.append([first, second, third, fourth]) 

with open('club_la_liga.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(x)