import random

all_employee={"name":"anmar","employee_id":"1"}
employee_numers=[1]
print("please fill up the information")

boolean=True
while boolean:
    try:
        name=input("Enter your name: ").lower().strip()
        id=int(input("national id numbers only : "))
    except ValueError:
        continue        
    else:
        genertae_id=random.randint(0,1)
        print(genertae_id)
        employee_numers.append(genertae_id)
        boolean=False


    if str(genertae_id) in all_employee["employee_id"]:
        print("The Generated employee number is taken start over ")
        boolean=True
        continue
    else: 
        all_employee={
            "name":name,
            "employee_id":genertae_id
        }
        print(all_employee)