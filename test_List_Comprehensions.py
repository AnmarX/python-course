# my_list=[1,2,3]
# double=[item*2 for item in my_list]
# # for item in my_list:
# #     double.append(item*2)
# print(double)

# users=[{'name':"nemo" ,'age':30},{'name':"nmr" ,'age':35},{'name':"alpha" ,'age':28}]
# user_name=[user['name'] for user in users if user['age']>30 and user['name']=='nmr']
# print(user_name)

# user_groub=[
#     [
#         {'name':'Anmar','age':23},
#         {'name':'nemo','age':18}
#     ]
# ,
#     [
#         {'name':'nmr','age':33},
#         {'name':'aboAlnmr','age':29}
#     ]
# ]

# user_name=[person['name'] for group in user_groub for person in group if person['age']>25]
# print(user_name)

#===============================
# given_list = [x for x in range(5)]
# print(given_list)

# #new_list = [var+3 for var in given_list]
# new_dict = {var:var + 3 for var in given_list }

# print(new_dict)
#===============================

# given_list = [x for x in range(5)]
# print(given_list)

# new_list = [var+3 for var in given_list]

# print(new_list)
#===============================

# list1 = [x for x in range(5)]
# list2 = ['Mon','Tue','Wed','Thu','Fri']
# print(list1)
# print(list2)

# new_dict ={key:value for (key, value) in zip(list1, list2)}

# print(new_dict)
#===============================

# given_set = {x for x in range(5)}
# print(given_set)

# new_set = {var+3 for var in given_set}

# print(new_set)
#===============================
given_list = [x for x in range(5)]
print(given_list)

new_set = (var+3 for var in given_list)

for var1 in new_set:
   print(var1, end=" ")