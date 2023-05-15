
#///json.load , load file into a python object , json.loads load string into a python object
#///json.dump , json.dump python object to a json file , json.dumps a python object into a json string

import requests
import json
from datetime import datetime
import smtplib
import time

print("start")
time.sleep(10)
print("end")


########ANGELA#########
# MY_EMAIL = "___YOUR_EMAIL_HERE____"
# MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude


# def is_iss_overhead():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()

#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])

#     #Your position is within +5 or -5 degrees of the iss position.
#     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
#         return True


# def is_night():
#     parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#     time_now = datetime.now().hour

#     if time_now >= sunset or time_now <= sunrise:
#         return True


# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
#         )
########ANGELA#########







# def f(fun):
#     def wrpper(x,y):
#         print("1")
#         ss=fun(x,y)
#         print("2")
#         return ss
#     return wrpper
# @f
# def hi(x,y):
#     print("hi")
#     return x+y
# print(hi(4,5))


# a=lambda x,y:x+y
# print(a(3,33))

# # #decorator 
# # #the first function take func as an arrgument 
# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper
# # #the first thing excuted 
# # #will return wapper so when you can say_hello function it's actually now the wrapper function 
# @my_decorator
# def say_hello():
#     print("Hello, world!")
# # #so when you call this will return def wrapper()
# say_hello()








# r=requests.get("http://api.open-notify.org/iss-now.json")
# data=r.json()
# q=json.dumps(data)
# print(q)


# response = requests.get('https://api.github.com/events')
# response.raise_for_status()
# if response.status_code==200:
#     print("done")
# data = response.json()[0]
# print(data)
# data2 = response.json()
# # #this will generate an error for some reason the endpoint will generate an erorr
# print(data2)
# q=json.dumps(data2)
# print(q)


# response = requests.get('https://api.github.com/events')
# # convert the response to JSON format
# json_data = json.loads(response.text)
# # print the JSON data
# print(json_data)



# a='''{
#     "name": "John Doe",
#     "age": 35,
#     "email": "johndoe@example.com",
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA",
#         "zip": "12345"
#     },
#     "phone_numbers": [
#         {
#             "type": "home",
#             "number": "555-1234"
#         },
#         {
#             "type": "work",
#             "number": "555-5678"
#         }
#     ],
#     "favorite_foods": [
#         "pizza",
#         "sushi",
#         "ice cream"
#     ],
#     "friends": [
#         {
#             "name": "Jane Doe",
#             "age": 30,
#             "email": "janedoe@example.com",
#             "address": {
#                 "street": "456 Oak St",
#                 "city": "Anytown",
#                 "state": "CA",
#                 "zip": "12345"
#             },
#             "phone_numbers": [
#                 {
#                     "type": "home",
#                     "number": "555-4321"
#                 },
#                 {
#                     "type": "work",
#                     "number": "555-8765"
#                 }
#             ],
#             "favorite_foods": [
#                 "tacos",
#                 "burritos",
#                 "guacamole"
#             ]
#         },
#         {
#             "name": "Bob Smith",
#             "age": 40,
#             "email": "bobsmith@example.com",
#             "address": {
#                 "street": "789 Elm St",
#                 "city": "Anytown",
#                 "state": "CA",
#                 "zip": "12345"
#             },
#             "phone_numbers": [
#                 {
#                     "type": "home",
#                     "number": "555-1111"
#                 },
#                 {
#                     "type": "work",
#                     "number": "555-2222"
#                 }
#             ],
#             "favorite_foods": [
#                 "steak",
#                 "potatoes",
#                 "beer"
#             ]
#         }
#     ]
# }'''
# print(a)
# print(json.loads(a))




# with open("delete.json","w")as f:
#     data=json.dump(a,f,indent=4)

# with open("delete.json","r")as f:
#     d=json.load(f)
#     print(d)

