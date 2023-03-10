from dbm import dumb
import json


from re import X
from tokenize import String
from unittest import result
import random
import turtle
import pandas 
import requests
import urllib
import csv
from ast import literal_eval

dictir=[
   
    {"countrey":"france",
    "cities":["paris","lyon"],
    "time_visited":4}
    ,
    {"countrey":"germany",
    "cities":["Munich","Frankfurt"],
    "time_visited":9}
]



  




# with open('mypickle.pickle', 'w') as f:
#     pickle.dump(dictir, f)





df = pandas.DataFrame(dictir) 
to_csv_file=df.to_csv ("data.csv")
rr=pandas.read_csv("data.csv",index_col=[0])
with open('fromcsv_toJSON.json','w') as a:
    ara=rr.to_json(a,orient="records",indent=4)
with open('fromcsv_toJSON.json','r') as a:
    dataa = json.load(a)
print(dataa[0])



# people = {
#           "first": {'name': 'John', 'age': '27', 'sex': 'Male',"subject":["sport","sience"]},
#           "scond": {'name': 'Marie', 'age': '22', 'sex': 'Female',"subject":["math","phyisics"]},
#           "third":{"name":"anmar","age":24,"sex":"male","subject":["math","sport"]}
#           }



# with open("developerDetailCompact.json", "w") as write_file:
#     json.dump(dictir, write_file,indent=4, separators=(',', ':'))



# data_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerows(data_list)

#/// first you get the info from an api as a json
r = requests.get('https://api.github.com/events')
js=r.json()
print(type(js))
#///this is wrong data=json.load(js)
#///second put the information on file 
with open("new_file.json","w") as aq:
  json.dump(js,aq,indent=2)
#///read the information from the file we have created 
with open('new_file.json') as f:
  data = json.load(f)
print(data[0]["actor"]["id"],data[0]["actor"]["login"])