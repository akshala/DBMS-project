from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path = '/home/akshala/Documents/IIITD/fourthSem/Misc/web scraping/chromedriver_linux64/chromedriver', chrome_options=option)
url = "https://www.transfermarkt.co.in/cristiano-ronaldo/profil/spieler/8198"
page = browser.get(url)

season_stats_elements = browser.find_elements_by_xpath("//a[@class='trackingLDWidget']")

season_stats = [x.text for x in season_stats_elements[6:12]]

print("Games ", season_stats[0])
print("Yellow cards ", season_stats[1])
print("Goals ", season_stats[2])
print("Second yellows ", season_stats[3])
print("Assists ", season_stats[4])
print("Red cards ", season_stats[5])
