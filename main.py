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

#### parsing data ####
def parse(data):
    #data = "JEZA425333, 4263 Otbah Ibn Aaed,qqqq" 
    new_list = []
    temp = ""
    for item in data.split(','):
        for sub_item in item.split():
            if sub_item.isdigit():
                # if temp:
                    # new_list.append(temp)
                # temp = ""
                new_list.append(sub_item)
            else:
                temp += ' ' + sub_item if temp else sub_item
        if temp:
            new_list.append(temp)
            temp = ""
    print(new_list)

parse("JEZA425333, 4263 Otbah Ibn Aaed,qqqq")
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
import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# first is the user will chose a coffe 

# then he will pay will money if he have enough money and we get the total money the person enterd he will get it if he doens't have enough money ge wont get the coffe also if the resource is not enough the person wont get the coffe

#if he does get the coffe our reoruces will decrease and will add the profit of the person got it 

#report to get the how much resource we got lift and how much i have earned

def calcMoney():
    money=0
    print("insert money for coffe")
    money+=int(input("How many 1 SR :"))* 1
    money+=int(input("How many 0.5 SR :"))* 0.5
    money+=int(input("How many 0.25 SR :"))* 0.25
    return money


def enough_money(money,dictResource):
    if money >= dictResource:
        global profit
        profit+=money
        return True
    else:
        print("not enough money")
        return False

def enough_resources(ingredients):
    
    for item in ingredients:
        if ingredients[item] > resources[item]:
            return False
    return True

def resource_decrease(order_ingredients):
    
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("ur coffe is served")

while True:
    user = input("​What would you like? (espresso/latte/cappuccino/exit): ")
    if user == "exit":
        sys.exit("")

    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}SR")
    
    else:
        if enough_resources(MENU[user]["ingredients"]):
            payment=calcMoney()
            if enough_money(payment,MENU[user]["cost"]):
                resource_decrease(MENU[user]["ingredients"])



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
#     "spec":"information technology",
#     "top3grade":["C","A+","B"]
    
#     },
# ]


# data=pandas.DataFrame(lest)
# data.to_csv("data.csv")
# rr=pandas.read_csv("data.csv",index_col=[0])

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

#------------------------------------day 30 json start---------------------------------
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
