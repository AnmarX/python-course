names=["anmar","rami","mohamed","nezar"]

def find(letter,data):
    out=[]
    for name in data:
        if name[0]==letter:
            out.append(name)
    return out
nameaa=find("n",names)
print(nameaa)


# names=["anmar","rami","noha","mohamed","nezar"]

# def find(letter,data):
#     out=[]
#     for name in data:
#         if name=="rami":
#             out.append(name)
#     return out

# nameaa=find("rami",names)
# print(nameaa)  
