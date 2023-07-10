import csv
import pandas
from csv import QUOTE_NONNUMERIC



with open("./from_31_to_60/company.csv") as file:
    r=pandas.read_csv(file,index_col=0)
    main=r["name"].to_list()
    # data=r["name"]
    # for l in r:
    #     print(l)

with open("./from_31_to_60/companyy.csv") as file:
    rr=pandas.read_csv(file,index_col=0)
    sub_main=rr["name"].to_list()

# #with list
unmatched=[]
for index,d in enumerate(sub_main):
    if d not in main:
        unmatched.append(index)


qq=[index for index in unmatched]
print(qq)



#with dict
unmatched={}
for index,d in enumerate(sub_main):
    if d not in main:
        unmatched[index]=d
        # unmatched[index]={
        #     "name":d
        # }



# qq={key:value for (key,value) in unmatched.items()}
# print(qq)







# unmatched_names = []
# for name in data:
#     if name not in dataa:
#         unmatched_names.append(name)

# # Print the unmatched names
# for name in unmatched_names:
#     print(name)





# unmatched_names ={}
# for d in data:
#     if d not in dataa:
#         for index , name in enumerate(data):
#             try:
#                 index = dataa.index(name)
#                 # print(index)
#             except ValueError:
#                 # #can be done in two ways
#                 # unmatched_names[index] = name
#                 unmatched_names[index]={
#                     "name":name
#                 }


# qq={key:value for (key,value) in unmatched_names.items()}
# print(qq)



# Print the unmatched names
# for name in unmatched_names.items():
#     print(name)


# if rr.equals(r):
#     print("true")
# else:
#     print("no")


# for value in data:
#     print(value)


# for index, value in enumerate(data):
#         print(f"{index}: {value}")