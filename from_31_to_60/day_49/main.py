from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
load_dotenv()
email=os.getenv("linkedin_email")
password=os.getenv("linkedin_pass")


'''fire fox driver'''
# #path="D:\firefox_driver\geckodriver"
# #ff = webdriver.Firefox()
# #ff.get('https://www.google.com')
'''fire fox driver'''
# #chrome_driver_path="D:\chrome_driver\chromedriver.exe"

driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs")
driver.fullscreen_window()
for_email=driver.find_element(by.CSS_SELECTOR,".text-input input")
for_email.send_keys(email)
time.sleep(60)