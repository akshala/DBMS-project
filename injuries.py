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
url = "https://www.transfermarkt.com/serie-a/verletztespieler/wettbewerb/IT1"
page = browser.get(url)

row = []
# row.append(["Player_Name","Injury_name","Due_date"])

name = browser.find_elements_by_xpath('//td[@class="hauptlink"]')
name = [x.text for x in name]
print(name)
n = len(name)

injury =  browser.find_elements_by_xpath("//td[@class='links']")
injury = [x.text for x in injury]
while (not injury):
    injury =  browser.find_elements_
    by_xpath("//td[@class='links']")
    injury = [x.text for x in injury]

print(injury)

due_date =  browser.find_elements_by_xpath("//td[@class='zentriert']")
due_date = [x.text for x in due_date]
while (not due_date):
    due_date =  browser.find_elements_
    by_xpath("//td[@class='links']")
    due_date = [x.text for x in due_date]
due_date = due_date[:n]
print(due_date)

n = len(name)
for i in range(n):
    row.append([name[i], injury[i], due_date[i]])
    # print(row)

with open('injury.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerows(row)