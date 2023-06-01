import smtplib
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
load_dotenv() 
email=os.getenv('my_gmail')
the_pass=os.getenv('password')
to_email=os.getenv('to_email')


res=requests.get("https://www.amazon.sa/-/en/gp/product/B07Y9Y69N7/ref=ox_sc_saved_image_1?smid=A13DHZ48BFXWO4&psc=1")

soup=BeautifulSoup(res.text,"html.parser")

#print(soup.prettify())

get_price=soup.select_one(".a-price-whole")
#print(get_price.text)

whole_price=get_price.text.split(".")[0]

print(whole_price)

price=475

if price > int(whole_price):
# #first create object of the email use with to close the connection after sending the email 
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        # securing the email from the man in the middle by encrypting the email (TLS) Transport Layer Security 
        connection.starttls()  
        # the password is from you google account to allow signing in your google account so you can send emails
        connection.login(user=email,password=the_pass)
        # send email method 1-(first the sender) 2-(then the resevier) 3-(the message)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg="Subject:from python\n\nthe keyborad has reached the required price buy now"
            )
else :
    pass