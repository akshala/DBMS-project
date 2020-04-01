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
url = "https://www.transfermarkt.co.in/premier-league/startseite/wettbewerb/GB1"
page = browser.get(url)

teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
# print(season_stats_elements)
teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

teamLinks = list(dict.fromkeys(teamLinks))
teamLinks = teamLinks[:20]
print(teamLinks)
row = []
row.append(["S.No","Name", "Games_Played","Goals","Assists","Yellow_cards","Red_cards","Club"])
cntt = 0
while (not teamLinks):
    teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
# print(season_stats_elements)
    teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

    teamLinks = list(dict.fromkeys(teamLinks))
    teamLinks = teamLinks[:20]
    # print(teamLinks)

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
    count = 0
    for j in playerLinks:
        print(count)
        count += 1
        try:
            url = j
            if(url == "https://www.transfermarkt.co.in/mix-diskerud/profil/spieler/103559"):
                continue
            if(url == "https://www.transfermarkt.co.in/nathaniel-clyne/profil/spieler/85177"):
                continue
            if(url == "https://www.transfermarkt.co.in/marco-van-ginkel/profil/spieler/147034"):
                continue
            if(url == "https://www.transfermarkt.co.in/phil-ofosu-ayeh/profil/spieler/133858"):
                continue
            if(url == "https://www.transfermarkt.co.in/david-brooks/profil/spieler/277033"):
                continue


            page = browser.get(url)
            season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")
        except:
            pass
        
        while(not season_stats_elements):   
            try:
                print(url)   
                url = j
                page = browser.get(url)
                season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")
            except:
                pass
        name = " ".join(list(map(lambda x:x.capitalize(), url.split("/")[3].split("-"))))
        club = " ".join(list(map(lambda x:x.capitalize(), i.split("/")[3].split("-"))))
        season_stats = [x.text for x in season_stats_elements[6:12]]
        cntt+=1
        row.append([cntt,name,season_stats[0],season_stats[1], season_stats[2], season_stats[4],season_stats[5], club])
        print(row)

with open('Seaon_player.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row)