from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

string="amazon"

driver=webdriver.Chrome()
driver.get("https://www.python.org/")
driver.fullscreen_window()
time.sleep(2)
search=driver.find_element(by.ID,"id-search-field")
search.send_keys(string)
time.sleep(10)
# #keys.enter = the enter key on the key board
#search.send_keys(Keys.ENTER)

