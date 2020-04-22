from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv
import pandas as pd
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path = '/home/akshala/Documents/IIITD/fourthSem/Misc/web scraping/chromedriver_linux64/chromedriver', chrome_options=option)
url = "https://www.transfermarkt.co.in/serie-a/gesamtspielplan/wettbewerb/IT1/saison_id/2019"
page = browser.get(url)

row = []

name = browser.find_elements_by_xpath('//a[@class="vereinprofil_tooltip tooltipstered"]')
name = [x.text for x in name]
teams = []
for elt in name:
	if len(elt):
		teams.append(elt)
print(teams)

home = []
away = []
n = len(teams)
i = 0
while i < n:
	home.append(teams[i])
	away.append(teams[i+1])
	i += 2

print("home:", home)
print("away:", away)

results = browser.find_elements_by_xpath('//td[@class="zentriert hauptlink"]')
results = [x.text for x in results]
print(results)

n = len(results)
row = []
row.append(['Home team', 'Away team', 'result'])
for i in range(n):
	row.append([home[i], away[i], results[i]])

with open('match_details_serie_A.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(row)

