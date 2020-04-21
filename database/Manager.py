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
url = "https://www.transfermarkt.com/primera-division/trainer/pokalwettbewerb/ES1"
page = browser.get(url)

teamLinks_elements = browser.find_elements_by_xpath("//a[@id='0']")
teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

teamLinks = list(dict.fromkeys(teamLinks))
teamLinks = teamLinks[:20]
teamLinks.append("https://www.transfermarkt.com/diego-simeone/profil/trainer/2868")
# teamLinks.append("https://www.transfermarkt.co.in/sinisa-mihajlovic/profil/trainer/3896")
# teamLinks.append("https://www.transfermarkt.co.in/antonio-conte/profil/trainer/3517")
print(teamLinks)
print(len(teamLinks))
managerRow = []
managerRow.append(["Manager_ID","Name","Age","Country","Formation","Contract","Win_Percentage"])
# cntt = 0
while (not teamLinks):
    teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
    teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

    teamLinks = list(dict.fromkeys(teamLinks))
    teamLinks = teamLinks[:20]
counter =40
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
            stats =  browser.find_elements_by_xpath("//td[@class='zentriert']")
            stats = [x.text for x in stats]
        winPercentage = int(stats[3])/int(stats[2])
        winPercentage = round(winPercentage*100,2)
        # ans = [managerID,name,age,country,formation,contract,winPercentage]
        # print(ans)
        print(str(managerID)+","+str(name)+","+str(age)+","+str(country)+","+str(formation)+","+str(contract)+","+str(winPercentage))
    except:
        pass