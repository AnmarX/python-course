MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(MENU["latte"]["ingredients"])

def get_desired_key(value_of_dictionary_key):
    # return [val for key, val in MENU.items()]
    r={(key if key == value_of_dictionary_key else None):val for key,val in MENU.items()}
  
    ## the output {"latte"}
    # r={key for key in MENU.keys()}

    ## the output {'ingredients': 'cost'}
    # r={key:value for key,value in MENU.values()}
    
    # rr="".join(r)
    # return "this issssss "+rr
    return r

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    print(get_desired_key(user_choice))

# result = [[a for a in range(1,3)] for _ in range(1,10)]

# print(result)
