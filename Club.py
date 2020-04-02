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

browser = webdriver.Chrome(executable_path = '/home/rachit/Downloads/chromedriver_linux64/chromedriver', chrome_options=option)
url = "https://www.transfermarkt.co.in/premier-league/startseite/wettbewerb/GB1"
page = browser.get(url)

teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

teamLinks = list(dict.fromkeys(teamLinks))
teamLinks = teamLinks[:20]
clubRow = []
managerRow = []
clubRow.append(["Club_name", "Manager_ID","League_name","Stadium"])
managerRow.append(["Manager_ID","Name","Country","Formation","Contract","Formation"])
cntt = 0
while (not teamLinks):
    teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
    teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

    teamLinks = list(dict.fromkeys(teamLinks))
    teamLinks = teamLinks[:20]
counter =0
for i in teamLinks:
    counter+=1
    try:
        url = i
        page = browser.get(url)
        stadium = browser.find_elements_by_xpath("//a[@id='"+url.split("/")[6]+"']")
        stadium = [x.get_attribute("text") for x in stadium]
        while (not stadium):
            stadium = browser.find_elements_by_xpath("//a[@id='"+url.split("/")[6]+"']")
            stadium = [x.get_attribute("text") for x in stadium]
        stadium = stadium[0]
        managerID = counter
        leagueName = "Premier League"
        club = " ".join(list(map(lambda x:x.capitalize(), i.split("/")[3].split("-"))))
        if (club[:2]=="Fc"):
            club = club[3:]
        print(club,managerID,leagueName,stadium)
    except:
        pass