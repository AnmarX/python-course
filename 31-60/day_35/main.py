from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()
api_key=os.getenv("weather_api_key")
account_sid=os.getenv("SID")
auth_token=os.getenv("twilio_token")
phone=os.getenv("phone")
twilio_phone=os.getenv("twilio_numer")



from twilio.rest import Client

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='last one',
    from_=twilio_phone,  # your Twilio phone number
    to= phone # recipient's phone number
)
print(message.status)
print(message.sid)


# parms={
#     "lat":51.507351,
#     "lon":-0.127758,
#     "appid":api_key
# } 
# r=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parms)
# print(r.text)



# params={
#     "q":"jeddah",
#     "appid":api_key
# }
# r=requests.get("https://api.openweathermap.org/data/2.5/weather",params=params)
# # aa=r.text
# # print(aa["coord"])
# # # use .json() when you want to access some data 
# a=r.json()
# print(a)
# print(a["coord"],a["weather"],a.get("main"))
# # #print(a)
# # print(json.dumps(a))




