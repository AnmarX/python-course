# from cgi import print_arguments
from dbm import dumb
import json
from re import X
from tokenize import String
from unittest import result
import random
import turtle
import urllib
import csv
from ast import literal_eval
from random import randint
import pandas
import requests

# #what join() function do
# l=["nemo","anmar"]
# aa="#".join(l)
# print(aa)


# #random.sample give it the list and how many char to take from the list 
###### password generator#######
# lower="qwertyuiopasdfghjklzxcvbnm"
# upper="QWERTYUIOPASDFGHJKLZXCVBNM"
# num="1234567890"
# symbols="[]{;/.<()-_=+`~|@#$%^&*}"
# all=lower+upper+num+symbols
# length=20
# # # .join will convert a list to a string and compain all the list values into one string
# # # example "".join(["A","B","C"]) output ABC
# password="".join(random.sample(all,length))
# print(password)
###### password generator#######


# def single(s):
#     counts={}

#     for c in s:
#         counts[c]=counts.get(c,0)+1
    
#     for c in counts:
#         if counts[c]==1:
#             return c
    

# print(single("aabbccq"))


# di={1:"nemo",2:"anmar"}
# for i in di:
#     print(i)
#### parsing data ####
# def parse(data):
#     #data = "JEZA425333, 4263 Otbah Ibn Aaed,qqqq" 
#     new_list = []
#     temp = ""
#     for item in data.split(','):
#         for sub_item in item.split():
#             if sub_item.isdigit():
#                 # if temp:
#                     # new_list.append(temp)
#                 # temp = ""
#                 new_list.append(sub_item)
#             else:
#                 temp += ' ' + sub_item if temp else sub_item
#         if temp:
#             new_list.append(temp)
#             temp = ""
#     print(new_list)

# parse("JEZA425333, 4263 Otbah Ibn Aaed,qqqq")
#### parsing data ####


#---------------------------------day 1 start-----------------------------------
#///if you dont want to get to the next line use end =""
#///if you use append it will add the whole word on a single index example ['nmr']
#///if you have name example "nmr" and you use += it will add every charcahter to a single index example ['n', 'm', 'r']
# qp=[]
# qp.append("nmr")
# qp+="Anmar"
# #/// brevios output  ['nmr', 'A', 'n', 'm', 'a', 'r'] 
# qp.insert(0,"done")
#///afther insert output ['done', 'nmr', 'A', 'n', 'm', 'a', 'r']
#///['done', 'nmr', 'A', 'n', 'm', 'a', 'r']
# del(qp[1])
#///['done', 'A', 'n', 'm', 'a', 'r']
#/// delete from index 1 to index 3
# del(qp[1:3])
# print(qp[2])
# print(qp)






# l=["anmr","4"]
# print(l)
# l[0]="nmr"
# print(l)


#///enumerate to list the index and the name on the list 
# /// if you want it without ()
# /// 0 apple
# /// 1 orange
# /// 2 mango
# /// 3 juice
# my_list = ["apple","orange","mango","juice"]
# for index, val in enumerate(my_list):
#     print(index, val)

#///if you want it with ()
#/// [0, 'apple']
#/// [1, 'orange']
#/// [2, 'mango']
#/// [3, 'juice']
# my_list = ["apple","orange","mango","juice"]
# for val in enumerate(my_list):
#     print(list(val))


# def fun(x):
#     print(x)

# num=3
# while num > 0:
#     fun(num)
#     fun("numbers")
#     num-=1 




#///continue if the condition is achived it will make u iterate again on the loop
# for x in range(3):
#     if x==1:
#         continue
#     else:
#         print("else")
# print("break done\n")
#///break if the condition is achived it bring u out of the loop
# for x in range(3):
#     if x==1:
#         break
#     else:
#         print("else")
# print("break done")

# x="Anmar"
# print("substring",x[1:3])
# print("substring",x[-3:])
# print("does it have?" , ("r" in x))
# input("enter name")
# print("jsj i")
# print("fjfj")


#///function
# def name(a,b,c):
#     return a+b+c
# print(name(2,3,4))

# class human:

#     def __init__(self,name,phone):
#         self.name=name
#         self.phone=phone
    
#     def get_name(self):
#         return self.name
#     def get_phone(self):
#         return self.phone

#     def set_phone(self,phone):
#         self.phone=phone
    
#     def set_name(self,name):
#         self.name=name
   
#     def random():
#         return 8

#     def __str__(self):
#         return "the name is ",self.name ," and my phone number is " ,self.phone
        
# d=human("anmar",7748747)
# print(d.get_name())
# print(d.__str__())
# print(human.random())
# d.set_name("nmr")
# print(d.get_name())

#///ما يروح للكود الي بعده وما ينفذ الكود كامل الا بعد ما تحط اسم 
# print("hello" + input("enter yournam: "))


# x=1
# z=2
#q=4
# a="ejn"
# print("anmar"+"qqq" , x +z , q)


#///this code is wrong u cant have 2 argument / an argument is the value inside the ()
#the + operator make 2 argument into 1 agrument
#the , operator make 2 sperate argument
#if you want to add a number to the text you need


#///worng code 
# a=5
# y="wrong also"
#u=input("duifhued",a)
#u=input("duifhued"+a)


#///correct code
#u=input("duifhued"+str(a))
#u=input("duifhued"+y)
#u=input("duifhued"+"hfiudf")


# a = input("a: ")
# b=input("b: ")
# temp=b
# b=a
# a=temp
# print(a)
# print(b)



# x=input("what is ur name: \n")
# y=input("what is ur city: \n")
# print(x,"live in",y)

#-------------------------------day 1 end--------------------------------------

#--------------------------------day 2 start-------------------------------------

#///type() to know the type of the data
#///you can conver int to string by using str() , int() ,foat()
# x=int(99.4)
# print("+",966_555_633_015)
# print(type(x))


# x=input("type 2 number here :\n")
#///type will be string from (x) so we will have to convert it to int and add them to each other
# print(type(x))
# print("hee"[2])
# first=x[0]
# second=x[1]
# resul=int(first)+int(second)
# print(resul)


# height=float(input("enter ur hight: "))
# weight=int(input("enter ur weight: "))
# BMI=int(weight)/float(height**2)
# print(int(BMI))


#f-string , this is how to use it 
# x=4
# y=7.8
# print(f"this is integer {x} and this is float {y}")


# age =input("enter ur age")
# age_int=int(age)
# yeras=90-age_int
# days=yeras*365
# week=yeras*52
# month=yeras*12
# print(f"you have {days} days , {week} weeks , {month} months remaining")


# b=int(input("nmber"))
# print(type(b))


#------------------------------------day 2 end---------------------------------

#------------------------------------day 3 start---------------------------------

# h=int(input("enter number : "))
# if h >100:
#     print("nice")
# elif h == 99:
#     print("done")
#     if h >45:
#         print("fjungi")
#     else:
#         print(5,"ok?")
# elif h < 50:
#     print("nmr")
#     if h>=600:
#         print("oooo")
#     else:
#         print("dfdfd")
# else:
#     print("oooooo")


#////you can also type it in this way and not use the round function/// print("your BMI ",int(BMI), "overweight")
# height=float(input("enter ur hight: "))
# weight=int(input("enter ur weight: "))
#///first way BMI=round(weight/height**2) but still the value in float 
#///second way below
# BMI=weight/height**2
# print(type(BMI))
# xxx=int(BMI)
# if xxx < 18.5:
#     print(f"your BMI {xxx} underweight")
# elif  18.5 < xxx < 25:
#     print(f"your BMI {xxx} NORMAL weight")
# elif 25 < xxx < 30:
#     print(f"your BMI {xxx} over weight")
# elif 30 < xxx < 35:
#     print(f"your BMI {xxx} obese")
# elif xxx > 35:
#     print(f"your BMI {xxx} clinically obese")


#count() function for counting how many time the letter have have been assigned 
# a="Anmar nabeel bably"
# print(a.count("a"))


# x=input("press A or B")
# if x.upper()=="A":
#     print("u pressed a")
#     if x.upper()=="A":
#         r=input("enter Q")
#         if r.upper()=="Q":
#             print("well done")
# else:
#     print("nothing was entered")
    
#------------------------------------day 3 end---------------------------------

#------------------------------------day 4 start---------------------------------

# x=random.randint(1,10)
# y=int(random.random()*10)
# print(x)
# print(test2.ppp ,test2.aaa)
# print(y)


# names=["anmar","nd","dofnhiud","oudfhu","fhdbdhi"]
# print(names)
# names[2]="dfoiif"
# print(names[0])
# names.append("kjgmofnmiom")
# print(names)
# names.extend(["nmr","lioeeo"])
# print(names)
#///if you want to get in without a function , so you can get the name and it's index use the method below 
#///len() is equall to .length in java 
# pqp=len(names)
# pp=random.randint(0,pqp -1)
# person=names[pp]
# print("the name is ",person," and the index of that number ",pp)
#///if you want to get random name from the array use random.choise below 
# fastrandom=random.choice(names)
# print(fastrandom)


# names=["anmar","nd","dofnhiud","oudfhu","fhdbdhi"]
# print(len(names)-1)
# print(names[3])

#/// nestes array 
# fruit=["apple","orange","grapes"]
# vegtebales=["corn","kale"]
# compined_array=[fruit,vegtebales]
# print(compined_array)
#///the first [] in nestes array to determine with array , and the next [] to determine with index in the array
# print(compined_array[0][2])


#you cant use int() before the input because if you want the first and the second index it have to be string first 
# o=input("enter number")
# print(type(o))
# x=int(o[0])
# y=int(o[1])
# print(type(x))
# fruit=["apple","orange","grapes"]
# vegtebales=["corn","kale","potato"]
# car=["nissan","dodge","toyota"]
# maps=[fruit,vegtebales,car]
# maps[x-1][y-1]="X"
#print(maps[x-1][y-1])
# print(f"{fruit}\n{vegtebales}\n{car}")


# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# else:
#     print(game_images[user_choice])
#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])
#     if user_choice == 0 and computer_choice == 2:
#      print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#      print("You lose")
#     elif computer_choice > user_choice:
#      print("You lose")
#     elif user_choice > computer_choice:
#      print("You win!")
#     elif computer_choice == user_choice:
#      print("It's a draw")



#------------------------------------day 4 end---------------------------------

#------------------------------------day 5 start---------------------------------

#/// we cant use range alone on list because we passing a list and range()expect int
#///calclauting the index , or getting the length of the list 
# fruits=["apple","oragne","grape","pie","mango","strayberry"]
# for fruit in range(0 ,len(fruits)):
#     print(fruit,end=" ")


#/// max(),min(),sum()
#///For example: ['175', '165', '185'].
#/// So simply said, it is a for loop where all items are converted into integers to be able to work within the challenge.
#/// So, there is for loop where the 'n' is the variable using inside the loop block.
#/// for n in range(0, len(student_heights)): range is another method with 2 parameters starting from 0 up to the length of our array excluded, n runs for n < 3.
#/// In our example: for n in range(0, 3):
#/// Then the first iteration n = 0: student_heights[0] = int(student_heights[0]) => student_heights[0] = int('175') so first element with index 0 = 175. The value 175 is assigned as the first element.
#/// Second iteration n = 1: student_heights[1] = int(student_heights[1]) => student_heights[1] = int('165'), second element of array will be 165 (integer).
#/// Last third iteration n = 2: student_heights[2] = int(student_heights[2]) => student_heights[2] = int('185'), third element with index = 2 will be 185 (integer). When n = 3 the for loop doesn't execute, the block o
# student_heights = input("Input a list of student heights ").split(" ")
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   print(student_heights[n],"and its index",n)
# length=0
# for height in student_heights:
#     length+=height
# print("total length of the stuednt: ",length,end=" ")
# numstu=0
# for number in student_heights:
#     numstu +=1
# print("the number of the student: ",numstu)


#///You cannot convert a list to an int. If you try to pass a list as an argument to the built-in int() method, you will raise the TypeError: int() argument must be a string, a bytes-like object or a number, not ‘list’.
#///first solution
# a_list = ["2", "4", "6", "8", "10"]
# int_list = list(map(int, a_list))
# print(int_list)
#second solution
# a_list = ["2", "4", "6", "8", "10"]
# int_list = [int(x) for x in a_list]
# print(int_list)


 
# total=0
# for number in range(2,101,2):
#     total +=number
# print(total)
#/// the third index (X,XXX,2) is for adding 
# for number in range(2,101,2):
#     print(number)



# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#///Eazy Level
# password = ""
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
# print(password)
#///Hard Level
# password_list = []
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# password = ""
# for char in password_list:
#   password += char
# print(f"Your password is: {password}")

#------------------------------------day 5 end---------------------------------


#------------------------------------day 7 start---------------------------------
# word_list=["ardvark","rami","ahmad"]

# while True:
#  new_name=input("if you want to add a new name press y if you dont press n: ").lower()
#  if new_name =="y":
#     for_the_name=input("enter the name you like: ").lower()
#     word_list.append(for_the_name)
#     print(word_list)
#     break
#  elif new_name=="n":
#     break
#  else:
#     print("enter the correct letter please")



# ran_choise=random.choice(word_list)
# lives=6
# print(f'the word is :{ran_choise}')
# display=[]

# for letter in range(len(ran_choise)):
#     display+="_"
# print(display)
# # end_of_game=False
# while True:
#  guess=input("guess a letter: ").lower()


# # # position will generate a number
#  for position in range(len(ran_choise)):
#     letter=ran_choise[position]

#     if letter==guess:
#      display[position]=letter


#  if guess not in ran_choise:
#     lives -=1
#     print(f'the lives you have left{lives}')
#     if lives ==0:
#         print("you lose")
#         break
  

#  print(display)
#  if "_" not in display:
#     print("you won")
#     break # end_of_game=True
  
#------------------------------------day 7 end---------------------------------


#------------------------------------day 8 start---------------------------------



# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# while direction =="encode" or direction=="decode":
#   break
# else:
#   print("wrong entery please re-enter the cipher!!")
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#  # #you can use list of a single word to get the index of the word
#  # #you dont need to use for loops only on list , dictitioary,etc..
#  # #you can use it also of words on any single word 
#  # #with using for loops like the example below , you are getting the index of that word
#  # # for letter in plain_text: if you wrote NMR is will loop through each letter N,M,R it will consider it a list
#   new_letter = ""
#   for letter in plain_text:
#    position = alphabet.index(letter)
#    new_position = position + shift_amount
#    new_letter += alphabet[new_position]
#   print(f"The encoded text is {new_letter}")

# def decrypt(cipher_text, shift_amount):
#    new_letter = ""
#    for letter in cipher_text:
#      position = alphabet.index(letter)
#      new_position = position - shift_amount
#      new_letter += alphabet[new_position]
#    print(f"The decoded text is {new_letter}")

# def caesar(cipher_text, shift_amount,ciper_direction):
#   new_letter = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     if ciper_direction=="encode":
#      new_position = position + shift_amount
#     elif ciper_direction=="decode":
#      new_position = position - shift_amount
#     new_letter += alphabet[new_position]


# caesar(text,shift,direction)
# if direction == "encode":
#   encrypt(text, shift)
# elif direction == "decode":
#   decrypt(text,shift)


#------------------------------------day 8 end---------------------------------




#------------------------------------day 9 start---------------------------------
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
#------------------------------------day 9  end---------------------------------


#------------------------------------day 10 start---------------------------------

# def add(n1, n2):
#   return n1 + n2
  
# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# def calculator():

#   num1 = float(input("What's the first number?: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True
#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#       should_continue = False
      
#       calculator()

# calculator()




#------------------------------------day 10 end-----------------------------------

#------------------------------------day 11 start-----------------------------------

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# #and returns the score. 
# #Look up the sum() function to help you do this.
# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

#   #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"


#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():


#   #Hint 5: Deal the user and computer 2 cards each using deal_card()
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#   while not is_game_over:
#     #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   play_game()

#------------------------------------day 11 end-------------------------------------


#------------------------------------day 12 start guessing game -------------------------------------


#Anmar solution start#
# def guessing(user_input):
#     if user_input ==computer:
#         print("'You got it right' ")
#     elif user_input > computer :
#         print("'To high' ") 
#     elif user_input < computer :
#         print("'To low'  ")


# def game(diffcality):
#     at_hard=5
#     at_easy=10
#     if diffcality == "hard":
#         while True:
#             try:
#                 user_input=int(input("\nguess a number from 0 to 20 :"))  
#             except ValueError:
#                 print("Please input integer only...")  
#                 continue
#             guessing(user_input)
#             at_hard-=1
#             if user_input == computer:
#                 #return and break will do the same thing exiting the loop
#                 break
#             elif at_hard==0:
#                 print("no attempet left you lost , the correct answer is",computer)
#                 return
#             elif user_input!=computer:
#                 print(f"\n attempet left {at_hard}")

         
#     elif diffcality == "easy":
#         while True:
#             try:
#                 user_input=int(input("\nguess a number from 0 to 20 :"))  
#             except ValueError:
#                 print("Please input integer only...")  
#                 continue
#             guessing(user_input)
#             at_easy-=1
#             print(f"\n attempet left {at_easy}\n")
#             if user_input == computer:
#                 #return and break will do the same thing exiting the loop
#                 break
#             elif at_easy==0:
#                 print("no attempet left you lost")
#                 return
#             elif user_input!=computer:
#                 print(f"\n attempet left {at_easy}")
         
        

#     elif diffcality !="easy" or diffcality !="hard":
#         print("wrong input re-enter the diffculaity\n")
#         diffcality=input("choise diffculity hard or easy : ").lower()
#         game(diffcality)
            


# print("\nWelcome to the gussing game \n")
# while True:
#     computer=random.choice(range(0,50))
#     diffcality=input("choise diffculity hard or easy : ").lower()
#     game(diffcality)
#     trying=input("want to play the guessing game again press 'yes' or 'no' ?").lower()
#     if trying=="yes".lower():
#       continue
#     else:
#         print("Thank you for playing this game , see you later")
#         exit()
# #Anmar solution end#


#Angela solution start#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()

#Angela solution end#






#------------------------------------day 12 end---------------------------------------




#------------------------------------day 13 start---------------------------------------



############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 19:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <=1994 :
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you?"))
# if age >= 18:
#     print(f"You can drive at age {age}.")
# else:
#     print("you cant drive")



# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page,"jnfiodgnfgnod")
# total_words = pages * word_per_page
# print(total_words)


# #Use a Debugger

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#------------------------------------day 13 end---------------------------------------




#------------------------------------day 14 start---------------------------------------

# nmr=('dffd','Vin', 'Diesel', '62')
# print(nmr[1]) # the index number 1
# print(nmr[1:])# all the elements except the first element  
# print(nmr[:1]) # only the first element 
# print(nmr[-1:])# only the last element 
# print(nmr[:-1]) # all the elemtns except the last element  
# to get the last key of a dict use list(dict.keys())[-1:]
# import random


# def thedata():
#     with open ("for_day_14.json") as celebrityFile:
#         data=json.load(celebrityFile)

#     ran=random.choice(data)
#     a=ran["name"]
#     b=ran["follower_count"]
#     # return f"{a} {b}"
#     return a,b
    


# boolean=True 
# point=0

# while boolean:
#     cho1=thedata()
#     name=cho1[0]
#     count=cho1[1]

#     print(count)

#     cho2=thedata()
#     name2=cho2[0]
#     count2=cho2[1] 

#     print(count2)

#     print(f"who has more follwers {name} or {name2}")
#     user=input("A OR B :").lower()
    
    
#     if user == "a".lower() and count > count2:
#         point+=1
#         print(f"ur score {point}")
#         continue

#     elif user == "b".lower() and count < count2:
#         point+=1
#         print(f"ur score {point}")
#         continue

#     else:
#         print("game over")
#         print(f"you got {point} score")
#         break




#solution 2
# def thename(gg):

#     namee=""
#     for lo in gg[:-1]:
#         namee+=lo+' '
        
#     return namee


# def thefollower(gg):
#     follower=""
#     for lo in gg[-1:]:
#         follower+=lo+' '
        
#     return follower



# point=0
# while True:

#     a=tuple(thedata().split())
#     b=tuple(thedata().split())


#     a_first=thename(a)
#     a_second=thefollower(a).strip()
    
#     print(a_second)

#     b_first=thename(b)
#     b_second=thefollower(b).strip()

#     print(b_second)
#     # print(a_first,a_second)
#     # print(b_first,b_second)

#     print(f"who has more follwers {a_first} or {b_first}")
#     user=input("A OR B :").lower()


    

#     if  a_second > b_second and user == "a".lower() :
#         point+=1
#         print(f"ur score {point}")
        

#     elif a_second < b_second and user == "b".lower():
#         point+=1
#         print(f"ur score {point}")
        

#     else:
#         print("game over")
#         print(f"you got {point} score")
#         break

    












#######ANGELA SOLUTION ##########
# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()
#######ANGELA SOLUTION ##########


#------------------------------------day 14 end---------------------------------------



#------------------------------------day 15 start---------------------------------------
# import sys
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# first is the user will chose a coffe 

# then he will pay will money if he have enough money and we get the total money the person enterd he will get it if he doens't have enough money ge wont get the coffe also if the resource is not enough the person wont get the coffe

#if he does get the coffe our reoruces will decrease and will add the profit of the person got it 

#report to get the how much resource we got lift and how much i have earned

# def calcMoney():
#     money=0
#     print("insert money for coffe")
#     money+=int(input("How many 1 SR :"))* 1
#     money+=int(input("How many 0.5 SR :"))* 0.5
#     money+=int(input("How many 0.25 SR :"))* 0.25
#     return money


# def enough_money(money,dictResource):
#     if money >= dictResource:
#         global profit
#         profit+=money
#         return True
#     else:
#         print("not enough money")
#         return False

# def enough_resources(ingredients):
    
#     for item in ingredients:
#         if ingredients[item] > resources[item]:
#             return False
#     return True

# def resource_decrease(order_ingredients):
    
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print("ur coffe is served")

# while True:
#     user = input("​What would you like? (espresso/latte/cappuccino/exit): ")
#     if user == "exit":
#         sys.exit("")

#     elif user == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: {profit}SR")
    
#     else:
#         if enough_resources(MENU[user]["ingredients"]):
#             payment=calcMoney()
#             if enough_money(payment,MENU[user]["cost"]):
#                 resource_decrease(MENU[user]["ingredients"])



# write a loop to go throgh all the resorces keys milk etc..
#test(resources,MENU[user]["ingredients"])
# print(resources)
# print(MENU["latte"]["ingredients"])
# for items in resources:
#     res=resources[items] - MENU["latte"]["ingredients"][items]
#     print(items,":",res)
# print(enough_money(calcMoney(),MENU[user]["cost"]))
# print(enough_resources(MENU[user]["ingredients"]))







############## angela ################
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
############## angela ################





#------------------------------------day 15 end---------------------------------------



#------------------------------------day 16 start---------------------------------------

########### playing with OOP ##################
# import sys
# class Student:
#     # #class attribute
#     num_of_student=0
#     # #class method is assosiated with the class atrribute not regular attribute
#     # #class method does not have anyt accosiation with the instance 
#     # #static method does not change any thing it's a function that can be used any time any where, for example def add()
#     @classmethod
#     def get_numberStu(cls):
#         return cls.num_of_student

#     @staticmethod
#     def add(x):
#         return x +1
#     # # Student.add(3)

#     @classmethod
#     def add_numberStu(cls):
#         cls.num_of_student +=1

#     def __init__(self,name,grade,age) -> None:
#         self.name=name
#         self.age=age
#         self.grade=grade
#         Student.add_numberStu()

#     def get_grade(self):
#         return self.grade
    
#     def get_stu_name(self):
#         return self.name


# class Allcourses:
#     """Models each Menu Item."""
#     def __init__(self, name,max_stu):
#         self.name = name
#         self.max_stu=max_stu
       
       


# class Course:
#     def __init__(self) -> None:
#         self.students=[]
#         self.allCourse = [
#             Allcourses(name="CPIT-455",max_stu=2),
#             Allcourses(name="CPIT-490",max_stu=3),
#             Allcourses(name="CPIT-405",max_stu=5)
#         ]
        

#     def add_student(self,student_obj,order_name):
#         ## this way works##
#         for stu in self.allCourse:
#             if stu.name.lower().strip() == order_name.lower().strip():
#                 if len(self.students) < stu.max_stu:
#                     self.students.append(student_obj)
#                     for student_num in range(len(self.students)):
#                         return self.students[student_num].name,True
                        
#         return False
#         ## this way also works##
#         # for stu in range(len(self.allCourse)):
#         #     if self.allCourse[stu].name.lower().strip() == order_name.lower().strip():
#         #         if len(self.students) < self.allCourse[stu].max_stu:
#         #             self.students.append(student_obj)
#         #             for student_num in range(len(self.students)):
#         #                 return self.students[student_num].name,True
                        
#         # return False
    
#     def get_average_grade(self):
#         value=0
#         for student in self.students:
#             value+=student.get_grade()
#         return value / len(self.students)
    
   
#     def choose_course(self):
#         options = ""
#         for item in self.allCourse:
#             options += f"{item.name}/"
#         return options
    
#     def find_course(self, order_name):
#         """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
#         for item in self.allCourse:
#             if item.name.lower().strip() == order_name.lower().strip():
#                 print("Course exists")
#                 return item
        
#         #print("Sorry that item is not available.")


#     def subject_and_name(self,student_obj,x):
#         try :
#             print(f"{student_obj.get_stu_name()},{self.find_course(x).name}")
#         except:
#             print("there is no course with this name")
        

#     def if_added(self,student_obj,order_name):
#         results=self.add_student(student_obj,order_name)
#         if results ==False:
#             print("student was not added for the course")
#         elif results[1] ==True:
#             print(f"student added,{results[0]} for course {order_name}")
                

        
        
#         # for a in range(len(self.students)):
#         #     #print(a)
#         #     if a < self.allCourse[a].max_stu:
#         #         print(f"student {self.students[a].name} is added to course {self.allCourse[a].name}")
#         #     if a == self.allCourse[a].max_stu-1:
#         #         print("the course is full")
#         #         return True
    
            
#     def not_added(self):
#         print("student not added")

# c=Course()
# x=input(f"choose course ({c.choose_course()})")
# s3=Student("nmr",80,20)
# #c.find_course(x)
# #stud=c.add_student(s3,x)
# c.subject_and_name(s3,x)
# #print(stud)
# c.if_added(s3,x)
# print(Student.get_numberStu())

# user=input("enter (exit) if you no longer want to add, enter (add) if you want to continue: ")

# while True:


#     if user == "exit".lower().strip():
#         sys.exit(0)
#     elif user == "add".lower().strip():
#         xx=input("write your name: ")
#         yy=int(input("write your grade: "))
#         zz=int(input("write your age: "))
#         s1=Student(xx,yy,zz)
        
#         x=input(f"choose course ({c.choose_course()})")
#         if not c.find_course(x):
#             pass
#         else:
#             c.add_student(s1) 

    
        



# c1=Course("CPIT-405",2)
# user=input("enter (exit) if you no longer want to add, enter (add) if you want to continue: ")
# while True:
#     if user == "exit".lower().strip():
#         sys.exit(0)
#     elif user == "add".lower().strip():
#         xx=input("write your name: ")
#         yy=int(input("write your grade: "))
#         zz=int(input("write your age: "))
#         s1=Student(xx,yy,zz)
#         c1.add_student(s1) 
       
#         if c1.if_added()== True:
#             print(Student.get_numberStu())
#             break

# s2=Student("nemo",77,27)
# s3=Student("nmr",80,20)
# c1.add_student(s1) 
# c1.add_student(s2) 
# c1.add_student(s3) 

#c1.if_added()
# for stu in range(len(c1.students)):





# nr=[["erer","ghhh"],["dfdf","dfdf"]]
# qq=len(nr)
# print(qq)
# for x in nr:
#     for y in x:
#         print(y)




# print(c1.get_studnets(),"\n")
# print(c1.students[0].name)
    




# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_name(self):
#         return self.name
    
#     def set_name(self,name):
#         self.name=name

#     def set_age(self,age):
#         self.age=age

#     def get_age(self):
#         return self.age
       

# h =Human("nmr",23)
# print(h.get_name())
# print(h.get_age())

# h.set_name("anmar")
# print(h.get_name())


# h2 =Human("too","40")
# print(h2.name)
########### playing with OOP ##################







############## angela ################
# class CoffeeMaker:
#     """Models the machine that makes the coffee"""
#     def __init__(self):
#         self.resources = {
#             "water": 300,
#             "milk": 200,
#             "coffee": 100,
#         }

#     def report(self):
#         """Prints a report of all resources."""
#         print(f"Water: {self.resources['water']}ml")
#         print(f"Milk: {self.resources['milk']}ml")
#         print(f"Coffee: {self.resources['coffee']}g")

#     def is_resource_sufficient(self, drink):
#         """Returns True when order can be made, False if ingredients are insufficient."""
#         can_make = True
#         for item in drink.ingredients:
#             if drink.ingredients[item] > self.resources[item]:
#                 print(f"Sorry there is not enough {item}.")
#                 can_make = False
#         return can_make

#     def make_coffee(self, order):
#         """Deducts the required ingredients from the resources."""
#         for item in order.ingredients:
#             self.resources[item] -= order.ingredients[item]
#         print(f"Here is your {order.name} ☕️. Enjoy!")



# class MenuItem:
#     """Models each Menu Item."""
#     def __init__(self, name, water, milk, coffee, cost):
#         self.name = name
#         self.cost = cost
#         self.ingredients = {
#             "water": water,
#             "milk": milk,
#             "coffee": coffee
#         }
#         print(self.ingredients)


# class Menu:
#     """Models the Menu with drinks."""
#     def __init__(self):
#         self.menu = [
#             MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
#             MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
#             MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
#         ]

#     def get_items(self):
#         """Returns all the names of the available menu items"""
#         options = ""
#         for item in self.menu:
#             options += f"{item.name}/"
#         return options

#     def find_drink(self, order_name):
#         """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
#         for item in self.menu:
#             if item.name == order_name:
                
#                 return item
#         print("Sorry that item is not available.")



# class MoneyMachine:

#     CURRENCY = "$"

#     COIN_VALUES = {
#         "quarters": 0.25,
#         "dimes": 0.10,
#         "nickles": 0.05,
#         "pennies": 0.01
#     }

#     def __init__(self):
#         self.profit = 0
#         self.money_received = 0

#     def report(self):
#         """Prints the current profit"""
#         print(f"Money: {self.CURRENCY}{self.profit}")

#     def process_coins(self):
#         """Returns the total calculated from coins inserted."""
#         print("Please insert coins.")
#         for coin in self.COIN_VALUES:
#             self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
#         return self.money_received

#     def make_payment(self, cost):
#         """Returns True when payment is accepted, or False if insufficient."""
#         self.process_coins()
#         if self.money_received >= cost:
#             change = round(self.money_received - cost, 2)
#             print(f"Here is {self.CURRENCY}{change} in change.")
#             self.profit += cost
#             self.money_received = 0
#             return True
#         else:
#             print("Sorry that's not enough money. Money refunded.")
#             self.money_received = 0
#             return False
        
# ## main ##
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()

# is_on = True

# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
        
#         drink = menu.find_drink(choice)
        
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#           coffee_maker.make_coffee(drink)
############## angela ################

#------------------------------------day 16 end---------------------------------------




#------------------------------------day 17 start---------------------------------------

# class User:
#     def __init__(self,name) -> None:
#         self.name=name
#         self.followers=0
#         self.following=0

#     def follow(self,user):
#         user.followers+=1
#         self.following+=1

# a=User("anmar")
# b=User("nemo")
# b.follow(a)
# a.follow(b)
# print(a.followers)
# print(a.following)

# print(b.followers)
# print(b.following)

# import random
# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]


# class Question:
    
#     def __init__(self,text,answer) -> None:
#         self.text=text
#         self.answer=answer

# class Quiz:
    

#     def __init__(self,q_list) -> None:
#         self.question_list = q_list
#         self.score=0
#         self.question_number = 0
        

#     def still_question_toGo(self):
#         return self.question_number < len(self.question_list)

#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
#         self.cheak_answer(user_answer, current_question.answer)
    
#     def cheak_answer(self,user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right!")
#         else:
#             print("That's wrong.")
#         print(f"The correct answer was: {correct_answer}.")
#         print(f"Your current score is: {self.score}/{self.question_number}\n")
        




# question_bank = []
# for l in range(len(question_data)):    
#     random_choise=random.choice(question_data)
#     text_ran=random_choise["text"]
#     answer_ran=random_choise["answer"]
#     question=Question(text_ran,answer_ran)
#     question_bank.append(question)
    
        
# quiz=Quiz(question_bank)

# while quiz.still_question_toGo():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    


  # boolean=input(f"Choose answer {text_ran} enter (True or False) ").lower().strip()
    # if boolean == answer_ran:
    #     pass
    # else:
    #     break
# ww=[]
# qq=[["Dfdf","TY","URT"],["Dfsdsdddf","sfsfsfTY","URsfsfsfT"]]
# cc=qq[0][0]="nemo"
# #print(qq)
# for l in qq:
#   for rr in l:
#     if rr == "TY":
#       ww.append(rr)
#       #ww.append(l)
#       print(l)
# print(ww)
    # for a in l:
#         g=l[1]
#         ww.append(g)
# print(ww)
# lst=[[1,2,3],[11,12,13],[21,22,23]]
# a=list(zip(*lst))[0]
# print(a)



############## angela ################

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]


# class Question:

#     def __init__(self, q_text, q_answer):
#         self.text = q_text
#         self.answer = q_answer

# class QuizBrain:

#     def __init__(self, q_list):
#         self.question_number = 0
#         self.score = 0
#         self.question_list = q_list

#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)

#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
#         self.check_answer(user_answer, current_question.answer)

#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right!")
#         else:
#             print("That's wrong.")
#         print(f"The correct answer was: {correct_answer}.")
#         print(f"Your current score is: {self.score}/{self.question_number}")
#         print("\n")

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
############## angela ################




#------------------------------------day 17 end---------------------------------------




#------------------------------------day 24 start---------------------------------



# s=["nemo"]

# for q in s:
#     print(q)

# PLACEHOLDER = "[name]"


# with open("./day_24/names.txt") as names_file:
    
#     names = names_file.readlines()
#     print(names)

# with open("./day_24/letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     print(letter_contents)
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         print(name)
#         with open(f"./day_24/letter_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)




#------------------------------------day 24 end ---------------------------------



#------------------------------------day 25 csv start---------------------------------
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()


# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)


#-m module-name Searches sys. path for the named module and runs the corresponding . py file as a script.



# lest=[
#     {"student":"anmar" ,
#     "score":"A+",
#     "GPA":4.20,
#     "spec":"information technology",
#     "top3grade":["D+","B+","C"]
#     }
#     ,
#     {"student":"nmr" ,
#     "score":"B+",
#     "GPA":4.88,
#     "spec":"computer scince",
#     "top3grade":["C","A+","B"]
    
#     },
# ]


# data_dict={
#     "students":["nemo","anmar","eerr"],
#     "scores":[70,80,90],
#     "subject":["cpit405","cpit490","cpit252"]
# }

# ds=pandas.DataFrame(data_dict)
# ds.to_csv("delete.csv")

# data=pandas.DataFrame(lest)


# print(data)
#yy=data.to_dict()
#print(yy)

#data.to_csv("data.csv")
#rr=pandas.read_csv("data.csv",index_col=[0])
# li=rr["score"].to_list()
# ss=rr["score"]
# print(ss)
# print(li)


##########################
# data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# qray=len(data[data["Primary Fur Color"]=="Gray"])
# red=len(data[data["Primary Fur Color"]=="Cinnamon"])
# black=len(data[data["Primary Fur Color"]=="Black"])

# for_dict={
#     "fur color":["qray","red","black"],
#     "count":[qray,red,black]
# }

# df=pandas.DataFrame(for_dict)
# df.to_csv("animals.csv")
# print(df)


# print(black)
# print(red)
# print(qray)


##########################
# df = pandas.DataFrame(
#     [["a", "b"], ["c", "d"]],
#     index=["row 1", "row 2"],
#     columns=["col 1", "col 2"],
# )
# result = df.to_json(orient="split")
# parsed = json.loads(result)
# hh=json.dumps(parsed, indent=4)  
# print(parsed)
# print(hh)

# #you can get the column with two methods
# #method number 1
#print(rr["spec"])
# #method number 2
#print(rr.spec)


# #get the data in row with two methods
# # method num 1
# print(rr[rr["spec"]=="information technology"])
# # # method num 2
# print(rr[rr.spec=="information technology"])
# stu1=rr[rr.spec=="information technology"]
# print(stu1.score)



#print(rr[["spec","student"]])
# def con(csv_path,json_path):
#     js=[]

#     with open(csv_path) as csvfile:
#         csvdata=csv.reader(csvfile)
#         for r in csvdata:
#           if r[0] !="id":
#             js.append({"id":r[0],"student":r[1],"score":r[2],"GPA":r[3],"spec":r[4],"top3grade":r[5]})


       
#     with open(json_path,'w') as jsfile:
#         jsfile.write(json.dumps(js,indent=2))

# csv_path='data.csv'
# json_path='jsonfile.json'

# con(csv_path,json_path)

# dictir=[
   
#     {"countrey":"france",
#     "cityes":["p","a","q"],
#     "times":7}
#     ,
#     {"countrey":"germeny",
#     "cityes":["p","a","q"],
#     "times":9}
# ]

# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(dictir)


# with open('data.csv', 'w', encoding='utf8', newline='') as output_file:
#     fc = csv.DictWriter(output_file,fieldnames=dictir[0].keys())            
#     fc.writeheader()
#     fc.writerows(dictir)

# keys = dictir[0].keys()
# with open('data.csv', 'w', newline='') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(dictir)




#///to remove the unamed raws u can use .read_csv("data.csv",index_col=[0]) 
#///or data.to_csv("data.csv, index=False")
##======================================
# data=pandas.DataFrame(dictir)
# data.to_csv("data.csv")
# rr=pandas.read_csv("data.csv",index_col=[0])


# with open('fromcsv_toJSON.json','w') as a:
#     ara=rr.to_json(a,indent=2,orient="records")
# # #qqq=pandas.read_json('fromcsv_toJSON.json')
# with open('fromcsv_toJSON.json','r') as a:
#     dataa = json.load(a)
##======================================
# # qr=rr.to_dict(orient="records")
# with open('fromcsv_toJSON.json','w') as a:
#   gg=a.write(json.dumps(qr,indent=4))
# with open('fromcsv_toJSON.json','r') as a:
#   dataa = json.load(a)
# print(dataa[0]["cityes"][0])

# fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# # csv data
# rows = [
#     {'name': 'Albania',
#     'area': ["434","66","22"],
#     'country_code2': 'AL',
#     'country_code3': 'ALB'},
#     {'name': 'Algeria',
#     'area':[2381741,545,64],
#     'country_code2': 'DZ',
#     'country_code3': 'DZA'},
#     {'name': 'American Samoa',
#     'area': [34656,33,77],
#     'country_code2': 'AS',
#     'country_code3': 'ASM'}
# ]

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(rows)






##with orient record use this
# print(dataa[0]['student'],dataa[0]['top3grade'][2],"\n")
#without orient record use this
# print(dataa['student']['0'],"\n")

#print(dataa)
#print(qqq)

# with open('fromcsv_toJSON.json') as a:
#      data = json.load(a)
# print(data)
##qqq=pandas.read_json('fromcsv_toJSON.json')
##print(qqq)
#print(data[0])

# print(rr,"\n")
# print(rr["student"])

#=======================================================
# #/// first you get the info from an api as a json
# r = requests.get('https://api.github.com/events')
# js=r.json()
# print(type(js))
# #///this is wrong data=json.load(js)
# #///second put the information on file 
# with open("new_file.json","w") as aq:
#   json.dump(js,aq,indent=2)
# #///read the information from the file we have created 
# with open('new_file.json') as f:
#   data = json.load(f)
# print(data[0]["actor"]["id"],data[0]["actor"]["login"])
#=======================================================





# data=pandas.read_csv("r.txt") 
# print(data["nmr"])

# cc=data.to_dict()
# print(cc)

# aa=data["nmr"].to_list()
# print(aa)


# dataf=[
#     {"student":["anmar","rami"],"scroe":[3,6,8],"scrofe":[3,6,8],"scroee":[3,6,8]},
#     {"teahcer":["math","scince"],"clases":["A","b","c"],"clases":["A","b","c"]}
#     ]

# data=pandas.DataFrame(dataf)

# data.to_csv("new.txt")


# #print(data)
# toread=pandas.read_csv("new.txt")

# print(toread)
#------------------------------------day 25 csv end---------------------------------




#------------------------------------day 26 start---------------------------------

#num=[1,2,3]
# li=[n+1 for n in num]
# print(li)

#li2=[n for n in num if n >=2 ]
#print(li2)


#num=[1,1,2,3,5,8,13,21,34,55]
# sq_num=[n*n for n in num]
# print(sq_num)

# num=[1,1,2,3,5,8,13,21,34,55]
# results=[n for n in num if n % 2==0]
# print(results)
 


#names=["anmar","nemo","mclaren"] 
# # # will get the values
# for l in names:
#     print(l)

# new_dict={student:random.randint(1,100) for student in names}
# print(new_dict)

# stu={student:score for (student,score) in new_dict.items() if score >= 50}
# print(stu)

#sentence="What is the Airspeed Velocity of an Unladen Swallow?"
# d={sn:len(sn) for sn in sentence.split()}
# print(d)

# weather={
# 'Monday': 53.6,
# 'Tuesday': 57.2,
# 'Wednesday': 59.0,
# 'Thursday': 57.2,
# 'Friday': 69.8,
# 'Saturday': 71.6,
# 'Sunday': 75.2
# }
# # #will only get the keys of the dict
# # for n in weather:
# #     print(n)
# new={day:round((degree*9/5)+32) for (day,degree) in weather.items()}
# print(new)


data_dict={
    "students":["nemo","anmar","eerr"],
    "scores":[70,80,90],
    "subject":["cpit405","cpit490","cpit252"]

}
# xx=input("enter name: ")
# for ah in data_dict:
#     if ah =="students":
#         namess=[oo for oo in data_dict[ah]]
#         print(namess)
#         namess.append(xx)
#         print(namess)

#         break


# student_records = { 
#     1:{
#         'john' : {'maths': 80, 'science': 90, 'english': 75},
#         'amy' : {'maths': 85, 'science': 92, 'english': 88},
#         'jessica' : {'maths': 90, 'science': 94, 'english': 76}
#     },
#     2:{
#         'john' : {'maths': 80, 'science': 90, 'english': 75},
#         'amy' : {'maths': 85, 'science': 92, 'english': 88},
#         'jessica' : {'maths': 90, 'science': 94, 'english': 76}}

# }


# qq=[1,2],[5,6]

# for i in student_records:
#     print(student_records[i]["amy"]["science"])
    

# testing=pandas.DataFrame(data_dict)
# print(testing)
# for (index,row) in testing.iterrows():
#     if row.scores <= 80:
#         print(row.students)
#     print(row.students)


# li=[["nemo","nemo2","nemo3"],["anmar"]]

# for q in li[0]:
#     if q=="nemo":
#         print(q)
    

#------------------------------------day 26 end---------------------------------



#------------------------------------day 27 start---------------------------------

####### ANGELA CODE######
# from tkinter import *

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# #Buttons
# def action():
#     print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
# ####### ANGELA CODE######



# ####### ANGELA CODE######

# from tkinter import *


# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)


# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

# #Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# #Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

# #Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)


# window.mainloop()
####### ANGELA CODE######




# from tkinter import * 
# win=Tk()
# win.title("first GUI program")
# win.minsize(width=500 , height=400)

# label=Label(text="label",font=("arial",24,"bold"))
# label.pack(side="top")

# #label.config(text="the newest")
# # label["text"]="new text"

# num=0
# def button_click():
#     global num
#     num+=1
#     print("i got clicked")
#     the_input=input.get()
#     label.config(text=f"i got clicked for the # time ={num} ,the changed name {the_input}")
   
    

# button=Button(text="click me",command=button_click)
# button.pack()

# input=Entry(width=40,)
# input.pack()
# # #the print wont work because the line is excuted before entering any input
# #print(input.get())

# text=Text(height=5,width=50) 
# text.pack()

# win.mainloop()


# #how to make default value
# def foo(a=3,b=6,c=9):
#     print(a,b,c)
# foo(a=10)


# #with only one * it will return type vale of a tuple 
# def foo(*args):
#     print("first argument",args[0])
#     sum=0
#     for n in args:
#         sum+=n
#     return sum
#     #print(args)
# print(foo(9,1,5,6,7,8,5,4,4,7,8))

# #with double ** it will return a tuple 
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
# myFun(first='Geeks', mid='for', last='Geeks')


# def concatenate(**kwargs):
#     print(kwargs)
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result
# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
 

# def foo2(**word):
#     print(word)
# foo2(first="dd",second=2,third=3)


# def foo(*key,a=10,**arg):
#     print(key,arg)
# foo(2,3,4,one=1)


# class car:
#     def __init__(self,**key) -> None:
#         # #if the attibute doesn't have value it will return error 
#         # #self.make=key["make"]
#         # #self.make=key["model"]

#         # #but using get if the attribute is empty it will return none
#         self.make=key.get("make")
#         self.model=key.get("model")

# c=car(make="nissan")
# print(c.make)


#------------------------------------day 27 end---------------------------------





#------------------------------------day 28 start---------------------------------
#######ANGELA#######
# from tkinter import *
# import math
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 1
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None

# # ---------------------------- TIMER RESET ------------------------------- # 

# def reset_timer():
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#     title_label.config(text="Timer")
#     check_marks.config(text="")
#     global reps
#     reps = 0


# # ---------------------------- TIMER MECHANISM ------------------------------- # 

# def start_timer():
#     global reps
#     reps += 1

#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60

#     if reps % 8 == 0:
#         count_down(long_break_sec)
#         title_label.config(text="Break", fg=RED)
#     elif reps % 2 == 0:
#         count_down(short_break_sec)
#         title_label.config(text="Break", fg=PINK)
#     else:
#         count_down(work_sec)
#         title_label.config(text="Work", fg=GREEN)


# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def count_down(count):

#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"

#     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count - 1)
#     else:
#         start_timer()
#         marks = ""
#         work_sessions = math.floor(reps/2)
#         for _ in range(work_sessions):
#             marks += "✔"
#         check_marks.config(text=marks)


# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)


# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
# title_label.grid(column=1, row=0)

# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=1)

# start_button = Button(text="Start", highlightthickness=0, command=start_timer)
# start_button.grid(column=0, row=2)

# reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
# reset_button.grid(column=2, row=2)

# check_marks = Label(fg=GREEN, bg=YELLOW)
# check_marks.grid(column=1, row=3)






# window.mainloop()
#######ANGELA#######

#------------------------------------day 28 end---------------------------------





#------------------------------------day 29 start---------------------------------
########ANGELA########
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# #Password Generator Project
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)

#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():

#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
#                                                       f"\nPassword: {password} \nIs it ok to save?")
#         if is_ok:
#             with open("data.txt", "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)


# # ---------------------------- UI SETUP ------------------------------- #

# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)

# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)

# #Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)

# #Entries
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "angela@gmail.com")
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)

# # Buttons
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)

# window.mainloop()
########ANGELA########

#------------------------------------day 29 end---------------------------------




#------------------------------------day 30 start---------------------------------

# try:
#     file=open("./0-30/data.csv")
# except:
#     file=open("./0-30/data.csv")
#     print("if the try had an error")
# # except FileNotFoundError:
# #     print("file not found")
# else:
#     print("nothing worng excuted")
# finally:
#     raise TypeError("made up error even if their isn't any error")



# fruits=["apple","pear","orange"]
# def make_pie(index):
#     try:
#         fruit=fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit+" pie")
# make_pie(2)


# facebook=[
#     {"likes":21,"comments":2},
#     {"likes":13,"comments":2,"shares":1},
#     {"likes":33,"comments":8,"shares":3},
#     {"comments":4,"shares":2},
#      {"comments":1,"shares":1},
#       {"likes":33,"comments":8}
# ]
# total_likes=0
# for post in facebook:
#     try:
#         total_likes+=post["likes"]
#     except KeyError:
#         pass
# print(total_likes)



  
data=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
# #the index is the number on the left (row)

dd={row.letter:row.code for (index,row) in data.iterrows()}
#this will work too but the previous one is for pandas library tomrowor
#dd={index:row for (index,row) in data.items()}
print(dd)
# x=input("write name: ").upper()
# ii=[["a","e","t"],["d","i"]]
# aa=["a","e","t"]
# print(aa[1])
# for q in aa:
#     print(q)
# for n in ii:
#     print(n)
#qq=[dd[letter] for letter in x]
#print(qq) 


# my_dict = {'apple': 2, 'banana': 3, 'cherry': 1, 'orange': 4}
# new_dict = {key.upper(): value for key,value in my_dict.items() if key.endswith('a')}
# print(new_dict)  # Output: {'APPLE': 2}





#response = requests.get('https://api.github.com/events')
# # input / {"name": "John", "age": 30, "city": "New York"} python object 
# #json.dumps a python object into a json formatted string
# #json.dumps() to serialize a Python dictionary to a JSON formatted string
# data=json.dumps(response.text)
# print(data)
# # output / '{"name": "John", "age": 30, "city": "New York"}' json string

# # input / '{"name": "John", "age": 30, "city": "New York"}' json string
# #json.loads load string into a python object
# #To deserialize a JSON formatted string to a python object
# data2=json.loads(data)
# print(data2)
# # output / {"name": "John", "age": 30, "city": "New York"} python object 





# #json.dump() is used to write a Python object (such as a dictionary, list, or string) to a JSON-formatted file or network stream. 
#my_dict = {"name": "John", "age": 30, "city": "New York"}
# Write my_dict to a JSON-formatted file
# with open("my_file.json", "w") as f:
#     json.dump(my_dict, f)



# #On the other hand, json.load() is used to read a JSON-formatted file or network stream into a Python object.
# Read JSON-formatted data from a file
# with open("my_file.json", "r") as f:
#     my_dict = json.load(f)

# print(my_dict)



# response = requests.get('https://api.github.com/events')
# # convert the response to JSON format
# json_data = json.loads(response.text)
# # print the JSON data
# print(json_data)






# make a request to the API
# response = requests.get('https://api.github.com/events')
# # open a file in write mode
# with open('posts.json', 'w') as file:
#     # write the response text to the file as JSON
#     json.dump(response.json(), file,indent=2)
# with open('posts.json',"r") as file:
#     print(json.load(file))


#///json.load , load file into a python object , json.loads load string into a python object
#///json.dump , json.dump python object to a json file , json.dumps a python object into a json string


# r = requests.get('https://api.github.com/events')
# js=r.json()
# # data=json.load(js)

# with open("new_file.json") as aq:
#   print(json.dumps(js,indent=2))
# print(dir(js))
# print(help(js))
# print(r.text)


#/// first you get the info from an api as a json
# r = requests.get('https://api.github.com/events')
# print(type(r))
# js=r.json()
# # print(type(js))
# #///this is wrong data=json.load(js)
# #///second put the information on file 
# with open("new_file.json","w") as aq:
#   json.dump(js,aq,indent=2)
# #///read the information from the file we have created 
# with open('new_file.json') as f:
#   data = json.load(f)
# print(data[0]["actor"]["id"],data[0]["actor"]["login"])


#///testing how dic works
# data={
#   "score":{"a":4.9,"b":3.9},
#   "amazon":{"c":33,"d":90}
# }

# data1={
#   "score":{
#     "a":4.9,
#     "b":3.9
#     },
#   "amazon":{
#       "allscore":{
#         "s":[80,90,87],
#         "r":"actor"     
#       }
#    }
# }



# print(data)
# print(data1["amazon"]["allscore"]["s"][0])







# with open('states.json') as f:
#   data = json.load(f)

# for state in data['states']:
#   qr=state["name"],state["abbreviation"]
#   print(qr)

# with open('new_states.json', 'w') as f:
#   json.dump(qr, f,indent=2)



#------------------------------------day 30 json end---------------------------------
