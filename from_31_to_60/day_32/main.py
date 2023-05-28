import smtplib
from dotenv import load_dotenv
import os
import socket
import datetime as dt
# load_dotenv() 
# email=os.getenv('my_gmail')
# the_pass=os.getenv('password')
# to_email=os.getenv('to_email')

# # gmail : smtp.gmail.com
# # hotmail : smtp.live.com
# # yahoo : smtp.mail.yahoo.com

# # first create object of the email use with to close the connection after sending the email 
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     # securing the email from the man in the middle by encrypting the email (TLS) Transport Layer Security 
#     connection.starttls()  
#     # the password is from you google account to allow signing in your google account so you can send emails
#     connection.login(user=email,password=the_pass)
#     # send email method 1-(first the sender) 2-(then the resevier) 3-(the message)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=to_email,
#         msg="Subject:from python\n\nThis is the body of my email."
#         )
    # no need for the line before the close() because we are using (with)
    # connection.close()


# now=dt.datetime.now()
# week_day=now.weekday()
# if week_day == 0:
#     with open("./31-60/day_32/quotes.txt","r") as file:
#         line=file.readlines()
#         print(line[1])
#         print("its the same")
# print(week_day)


# now=dt.datetime.now()
# print(now)
# year=now.year
# print(year)
# month=now.month
# print(month)
# date=now.date()
# print(date)
# day=now.day
# print(day)
# time=now.time()
# print(time)
# week_day=now.weekday()
# print(week_day)
# date_of_birth=dt.datetime(year=1999,month=5,day=1)
# print(date_of_birth)



from dotenv import load_dotenv
from datetime import datetime
import pandas
import random
import smtplib


load_dotenv() 
MY_EMAIL=os.getenv('my_gmail')
MY_PASSWORD=os.getenv('password')
#to_email=os.getenv('to_email')


# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"


today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
# # you can use tuple as a key because its hashable
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
''' the outpur of  birthdays_dict right here the tuple is the key 
{(5, 9): name                  anmar
email    dvil1exp@gmail.com
year                   1999
month                     5
day                       9
Name: 0, dtype: object}
'''
# # this will get the dict with the key
print(birthdays_dict)
if today_tuple in birthdays_dict:
    # # this will get the dict without the key only the values
    birthday_person = birthdays_dict[today_tuple]
    ''' the output of birthday_person
    name                  anmar
    email    dvil1exp@gmail.com
    year                   1999
    month                     5
    day                       9
    Name: 0, dtype: object
    '''
    '''right here its a dict so we will consider the python object on the left is the key and on the right is the value'''
    # print(birthday_person)
    # # #example:
    # print(birthday_person["name"])
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )






# import random

# # Define a list of items to choose from
# fruits = ['apple', 'banana', 'cherry', 'durian', 'elderberry']

# # Choose three random fruits with replacement
# random_fruits = random.choices(fruits, k=1)

# print(random_fruits)

    

