import if_main_2 as model


"""if i comment the line below it will not run because if using if __name__ on the model
but if i remove the __name__ on the other model even though the line below is a comment it will run it from the import 
"""
#print(model.x())
# print("func")




# # module.py
# print("This code will be executed upon import.")

# def my_function():
#     print("This code will not be executed upon import.")

# # main.py
# import module

# print("Import successful.")

# module.my_function()

"""When you run main.py, it will first execute the code in module.py upon import, which will print "This code will be executed upon import."
Then, it will print "Import successful." After that, when you call module.my_function(),
it will execute the code inside the function and print "This code will not be executed upon import."

So, when you import a module from another file, the code outside of function or class definitions will run, 
but any code inside functions or classes will only run when explicitly called."""
