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
# url = "htt/ps://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1"
# page = browser.get(url)

# teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
# print(season_stats_elements)
# teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

# teamLinks = list(dict.fromkeys(teamLinks))
# teamLinks = teamLinks[:20]
# print(teamLinks)
row = []
# row.append(["S.No","Name", "Games_Played","Goals","Assists","Yellow_cards","Red_cards","Club"])
cntt = 1024
# while (not teamLinks):
#     teamLinks_elements = browser.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
# # print(season_stats_elements)
#     teamLinks = [x.get_attribute("href") for x in teamLinks_elements]

#     teamLinks = list(dict.fromkeys(teamLinks))
#     teamLinks = teamLinks[:20]
#     print(teamLinks)

#     playerLinks_elements = []
teamLinks = ['https://www.transfermarkt.com/real-madrid/startseite/verein/418/saison_id/2019', 'https://www.transfermarkt.com/fc-barcelona/startseite/verein/131/saison_id/2019', 'https://www.transfermarkt.com/atletico-madrid/startseite/verein/13/saison_id/2019', 'https://www.transfermarkt.com/fc-valencia/startseite/verein/1049/saison_id/2019', 'https://www.transfermarkt.com/real-sociedad-san-sebastian/startseite/verein/681/saison_id/2019', 'https://www.transfermarkt.com/fc-sevilla/startseite/verein/368/saison_id/2019', 'https://www.transfermarkt.com/real-betis-sevilla/startseite/verein/150/saison_id/2019', 'https://www.transfermarkt.com/athletic-bilbao/startseite/verein/621/saison_id/2019', 'https://www.transfermarkt.com/fc-villarreal/startseite/verein/1050/saison_id/2019', 'https://www.transfermarkt.com/fc-getafe/startseite/verein/3709/saison_id/2019', 'https://www.transfermarkt.com/celta-vigo/startseite/verein/940/saison_id/2019', 'https://www.transfermarkt.com/espanyol-barcelona/startseite/verein/714/saison_id/2019', 'https://www.transfermarkt.com/deportivo-alaves/startseite/verein/1108/saison_id/2019', 'https://www.transfermarkt.com/ud-levante/startseite/verein/3368/saison_id/2019', 'https://www.transfermarkt.com/cd-leganes/startseite/verein/1244/saison_id/2019', 'https://www.transfermarkt.com/real-valladolid/startseite/verein/366/saison_id/2019', 'https://www.transfermarkt.com/rcd-mallorca/startseite/verein/237/saison_id/2019', 'https://www.transfermarkt.com/ca-osasuna/startseite/verein/331/saison_id/2019', 'https://www.transfermarkt.com/sd-eibar/startseite/verein/1533/saison_id/2019', 'https://www.transfermarkt.com/fc-granada/startseite/verein/16795/saison_id/2019']

for i in teamLinks:
    # try:
    url = i
    page = browser.get(url)
    playerLinks_elements = browser.find_elements_by_xpath("//a[@class='spielprofil_tooltip tooltipstered']")
    # print("yo")
        # playerLinks= [x.get_attribute("href") for x in playerLinks_elements]
    # except:
        # pass
    while(not playerLinks_elements):
        url = i
        page = browser.get(url)
        print("yo")
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
            # if(url == "https://www.transfermarkt.co.in/mix-diskerud/profil/spieler/103559"):
            #     continue
            # if(url == "https://www.transfermarkt.co.in/nathaniel-clyne/profil/spieler/85177"):
            #     continue
            # if(url == "https://www.transfermarkt.co.in/marco-van-ginkel/profil/spieler/147034"):
            #     continue
            # if(url == "https://www.transfermarkt.co.in/phil-ofosu-ayeh/profil/spieler/133858"):
            #     continue
            # if(url == "https://www.transfermarkt.co.in/david-brooks/profil/spieler/277033"):
            #     continue
            # if(url == "https://www.transfermarkt.co.in/jack-colback/profil/spieler/61644"):
            #     continue

            page = browser.get(url)
            season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")
        except:
            pass
        maxRetries = 0
        boxEmpty = False
        while(not season_stats_elements):   
            try:
                # print(url)   
                url = j
                page = browser.get(url)
                season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")
                print(season_stats_elements)
                maxRetries+=1
            except:
                pass
            if maxRetries>=2:
                boxEmpty = True
                break
        if (boxEmpty):
            continue
        name = " ".join(list(map(lambda x:x.capitalize(), url.split("/")[3].split("-"))))
        club = " ".join(list(map(lambda x:x.capitalize(), i.split("/")[3].split("-"))))
        if (club[:2]=="Fc"):
            club = club[3:]
        season_stats = [x.text for x in season_stats_elements[6:12]]
        cntt+=1
        row.append([cntt,name,season_stats[0], season_stats[2],season_stats[-2],season_stats[1],season_stats[-1], club])
        print(row)

with open('Seaon_player_la_liga.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row)