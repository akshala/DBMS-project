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
url = "https://www.transfermarkt.com/la-liga/trainer/pokalwettbewerb/GB1"
page = browser.get(url)

teamLinks_elements = browser.find_elements_by_xpath("//a[@id='0']")
teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

teamLinks = list(dict.fromkeys(teamLinks))
teamLinks = teamLinks[:20]
teamLinks.append("https://www.transfermarkt.com/jurgen-klopp/stationen/trainer/118/plus/1")
teamLinks.append("https://www.transfermarkt.com/ralph-hasenhuttl/profil/trainer/2300")
print(teamLinks)
managerRow = []
managerRow.append(["Manager_ID","Name","Age","Country","Formation","Contract","Win_Percentage"])
# cntt = 0
row = []
row.append(["ManagerID", "Name", "Age", "Country", "Formation", "Contract", "winPercentage"])
while (not teamLinks):
    teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
    teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

    teamLinks = list(dict.fromkeys(teamLinks))
    teamLinks = teamLinks[:20]
counter =0
for i in teamLinks:
    counter+=1
    try:
        url = i+"/plus/1"
        page = browser.get(url)
        name = " ".join(list(map(lambda x:x.capitalize(), i.split("/")[3].split("-"))))
        managerID =counter
        data = browser.find_elements_by_xpath("//span[@class='dataValue']")
        data = [x.text for x in data]
        while (not data):
            data = browser.find_elements_by_xpath("//span[@class='dataValue']")
            data = [x.text for x in data]
        country = data[2]
        age = data[0].split(",")[1][7:-1]
        formation = data[-5].split()[0]
        contract = data[-2]

        
        stats =  browser.find_elements_by_xpath("//td[@class='zentriert']")
        stats = [x.text for x in stats]
        while (not stats):
            stats =  browser.find_elements_
            by_xpath("//td[@class='zentriert']")
            stats = [x.text for x in stats]
        winPercentage = int(stats[3])/int(stats[2])
        winPercentage = round(winPercentage*100,2)
        row.append([managerID,name,age,country,formation,contract,winPercentage])
        print(row)
    except:
        pass

with open('manager_la_liga.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(row)