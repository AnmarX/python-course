from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path="D:\chrome_driver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.google.com/webhp?authuser=1")
driver.fullscreen_window()
search=driver.find_element(by.ID,"APjFqb")
time.sleep(3)
search.send_keys("python")
search.send_keys(Keys.ENTER)
time.sleep(5)

a=driver.find_element(by.CSS_SELECTOR,".yuRUbf a h3")
a.click()
time.sleep(3)

k=driver.find_element(by.ID,"id-search-field")
k.send_keys("python")
k.send_keys(Keys.ENTER)
time.sleep(3)







###########ANGELA########## 
#https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b
###########ANGELA##########


# chrome_driver_path="D:\chrome_driver\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.python.org/")

# def get_index(date,index):
#     first=date[index] 
#     d=first.get_attribute("datetime").split("T")[0]
#     return d


# chrome_driver_path="D:\chrome_driver\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.python.org/")

# # year=driver.find_element(by.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# year=driver.find_elements(by.CSS_SELECTOR,'.event-widget time')
# name=driver.find_elements(by.CSS_SELECTOR,'.event-widget a')


# # first=year[0]
# # d=first.get_attribute("datetime").split("T")[0]

# upcoming_events={
#     1:{"time":get_index(year,0),
#        "name":name[1].text

#     },
#     2:{"time":get_index(year,1),
#        "name":name[2].text
        
#     },
#     3:{"time":get_index(year,2),
#        "name":name[3].text

#     },
#     4:{"time":get_index(year,3),
#        "name":name[4].text
        
#     },
#     5:{"time":get_index(year,4),
#        "name":name[5].text

#     }
    
# }

# print("\n",upcoming_events)
# # d=year.get_attribute("datetime")
# # print(d.split("T")[0])

# ######ANGELA######
# events_time=driver.find_elements(by.CSS_SELECTOR,".event-widget time")
# evetns_name=driver.find_elements(by.CSS_SELECTOR,".event-widget a")

# events={}

# for n in range(len(events_time)):
#     events[n]={
#         "time":events_time[n].text,
#         "name":evetns_name[n].text

#     }
# ######ANGELA######







# chrome_driver_path="D:\chrome_driver\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.sa/-/en/Keyboard-Membrane-Ultra-Compact-Waterproof-Computer/dp/B0BKLC5MTT/ref=sr_1_8?crid=3E53IML7SHZO2&keywords=keybord&qid=1685980161&sprefix=keybord%2Caps%2C215&sr=8-8")
# price=driver.find_element(by.CLASS_NAME,"a-price-whole")

# attibute=driver.find_element(by.ID,"add-to-cart-button")
# val=attibute.get_attribute("value")

## logo.size
#driver.find_element(by.CSS_SELECTOR,)
#driver.find_element(by.XPATH,)
# print("\n###################################")
# print(attibute.tag_name)
# print(val)
# print(price.text)


# driver.close()
# driver.quit()