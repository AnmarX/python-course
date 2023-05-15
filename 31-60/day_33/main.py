
#///json.load , load file into a python object , json.loads load string into a python object
#///json.dump , json.dump python object to a json file , json.dumps a python object into a json string

import requests
import json



def f(fun):
    def wrpper(x,y):
        print("1")
        ss=fun(x,y)
        print("2")
        return ss
    return wrpper
@f
def hi(x,y):
    print("hi")
    return x+y
print(hi(4,5))


a=lambda x,y:x+y

print(a(3,33))

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

