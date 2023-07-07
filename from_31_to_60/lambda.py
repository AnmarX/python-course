def fun(my_func,iteration):
    result=[]
    for item in iteration:
        new_item=my_func(item)
        result.append(new_item)
    return result




num=[1,4,6,22]

aa=fun(lambda item:item*item,num)
print(aa)