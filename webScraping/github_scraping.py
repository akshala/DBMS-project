from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path = 'enter path for chrome driver', chrome_options = option)
github_handle = input("Enter github handle ")

url = "https://github.com/" + github_handle 
page = browser.get(url)

titles_element = browser.find_elements_by_xpath("//a[@class='text-bold flex-auto min-width-0 ']")

titles = [x.text for x in titles_element]

print('TITLES:')
print(titles, '\n')

language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element]

print("LANGUAGES:")
print(languages, '\n')

for title, language in zip(titles, languages):
	print("RepoName : Language")
	print(title + ": " + language, '\n')