# #print(" In the decorators files")


# def add(a, b): 
#     return a + b 


# sum = add(4, 3)


# print("After assigning add to sum")
# sum()
# print("After calling sum")






# def add(a, b): 
#     return a + b

# sum = add

# print(sum(4, 3))




# def parent():
#     print("I am a parent")

#     def child():
#         print("I am a child")

#     child()

# parent()

def outer():
    def inner():
         print("Python is cool")

    return inner

my_func = outer()
my_func()