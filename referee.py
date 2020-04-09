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
url = "https://www.transfermarkt.co.in/serie-a/schiedsrichter/wettbewerb/IT1/plus/?saison_id=all"
page = browser.get(url)

row = []
row.append(["Referee_ID","Name","League_name", "yellow_cards","red_cards","penalties_given"])

name = browser.find_elements_by_xpath('//td[@class="hauptlink"]')
name = [x.text for x in name]
print(name)

stats =  browser.find_elements_by_xpath("//td[@class='zentriert']")
stats = [x.text for x in stats]
while (not stats):
    stats =  browser.find_elements_
    by_xpath("//td[@class='zentriert']")
    stats = [x.text for x in stats]

def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

stats = list(divide_chunks(stats, 6))
print(stats)

n = len(name)
for i in range(n):
    row.append([i+51, name[i], "Serie A", stats[i][2], stats[i][4], stats[i][5]])
    # print(row)

with open('referee.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerows(row)