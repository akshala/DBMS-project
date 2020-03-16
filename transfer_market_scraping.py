from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path = '/home/rachit/Downloads/chromedriver_linux64/chromedriver', chrome_options=option)
url = "https://www.transfermarkt.co.in/premier-league/startseite/wettbewerb/GB1"
page = browser.get(url)

teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
# print(season_stats_elements)
teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

teamLinks = list(dict.fromkeys(teamLinks))
teamLinks = teamLinks[:20]
print(teamLinks)

while (not teamLinks):
    teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
# print(season_stats_elements)
    teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

    teamLinks = list(dict.fromkeys(teamLinks))
    teamLinks = teamLinks[:20]
    print(teamLinks)

    playerLinks_elements = []
for i in teamLinks:
    try:
        url = i
        page = browser.get(url)
        playerLinks_elements = browser.find_elements_by_xpath("//a[@class='spielprofil_tooltip tooltipstered']")

        # playerLinks= [x.get_attribute("href") for x in playerLinks_elements]
    except:
        pass
    while(not playerLinks_elements):
        url = i
        page = browser.get(url)
        playerLinks_elements = browser.find_elements_by_xpath("//a[@class='spielprofil_tooltip tooltipstered']")

    playerLinks= [x.get_attribute("href") for x in playerLinks_elements]
    playerLinks = list(dict.fromkeys(playerLinks))
    season_stats_elements = []
    for j in playerLinks:
        try:
            url = j
            page = browser.get(url)
            season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")
        except:
            pass
        
        while(not season_stats_elements):   
            try:
                print("tadaaaa")    
                url = j
                page = browser.get(url)
                season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")
            except:
                pass

        season_stats = [x.text for x in season_stats_elements[6:12]]

        print("Games ", season_stats[0])
        print("Yellow cards ", season_stats[1])
        print("Goals ", season_stats[2])
        print("Second yellows ", season_stats[3])
        print("Assists ", season_stats[4])
        print("Red cards ", season_stats[5])
