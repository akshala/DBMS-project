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
clubRow.append(["Club_name", "League_position","Matches_played","Matches_won","Matches_lost","Goals_For","Goals_Against","Season_Year"])

url = "https://www.transfermarkt.co.in/premier-league/tabelle/wettbewerb/GB1/saison_id/2019"
page = browser.get(url)

for a in range(3):
    if (a==1):
        url = "https://www.transfermarkt.co.in/seriea/tabelle/wettbewerb/IT1/saison_id/2019"
        page = browser.get(url)
    elif (a==2):
        url = "https://www.transfermarkt.co.in/la-liga/tabelle/wettbewerb/ES1/saison_id/2019"
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
    # print(team    Links)

    dataTable =browser.find_elements_by_xpath("//td[@class='zentriert']")
    dataTable = [x.text for x in dataTable]
    # print(dataTable)
    for iz in range(len(teamLinks)):
        i = teamLinks[iz]
        club = " ".join(list(map(lambda x:x.capitalize(), i.split("/")[3].split("-"))))
        if (club[:2]=="Fc"):
            club = club[3:]
            # dataTable =browser.find_elements_by_xpath("//td[@class='zentriert']")
        # dataTable = [x.text for x in dataTable]
        # print(club)
        t = dataTable[iz*7:7*iz+7]
        matches = t[0]
        wins = t[1]
        losses = t[3]
        goalsFor = t[4].split(":")[0]
        goalsAgainst = t[4].split(":")[1]
        leaguePos = iz+1
        year = 2019
        clubRow.append([club,leaguePos,matches,wins,losses,goalsFor,goalsAgainst,year])

with open('SeasonClub.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(clubRow)