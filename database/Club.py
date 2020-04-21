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

clubRow = []
# managerRow = /[]
clubRow.append(["Club_name", "Manager_ID","League_name","Stadium"])
# managerRow.append(["Manager_ID","Name","Country","Formation","Contract","Formation"])
cntt = ""
url = "https://www.transfermarkt.com/primera-division/startseite/wettbewerb/ES1"
page = browser.get(url)

teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

teamLinks = list(dict.fromkeys(teamLinks))
teamLinks = teamLinks[:20]
while (not teamLinks):
    teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
    teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

    teamLinks = list(dict.fromkeys(teamLinks))
    teamLinks = teamLinks[:20]
print(teamLinks)
for i in teamLinks:
    # print(i)
    # cntt+=1
    url = i
    # print('here')
    page = browser.get(url)
    try:

        # print("hrllo")
        stadium = browser.find_elements_by_xpath("//a[@id='"+url.split("/")[6]+"']")
        stadium = [x.get_attribute("text") for x in stadium]
        while (not stadium):
            # print("ffs")
            stadium = browser.find_elements_by_xpath("//a[@id='"+url.split("/")[6]+"']")
            stadium = [x.get_attribute("text") for x in stadium]
        stadium = stadium[0]
        managerID = cntt
        leagueName = "La Liga"
        club = " ".join(list(map(lambda x:x.capitalize(), i.split("/")[3].split("-"))))
        if (club[:2]=="Fc"):
            club = club[3:]
        
        print(str(club)+","+str(managerID)+","+str(leagueName)+","+str(stadium))
    except:
        pass