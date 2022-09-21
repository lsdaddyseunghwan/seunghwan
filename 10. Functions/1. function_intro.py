# When we want to reuse the piece of code or algorithm,
# we create functions and reuse them.

# syntax of creating a method is-> def method_name.

def print_name():
    print("Techtorial.")

# Method only work when they get called.
print_name()

# Let's create a method for greeting.
# It will take user's name as argument and will print,
# Hello User's Name

def print_greeting(name):
    print(f"Hello {name}")

print("Enter your name")
user_name=input()
print_greeting(user_name)

print(type(print_greeting(user_name)))
# print(type(user_name.lower()))
def get_greeting(name):
    return f"Hello {name}"
# Method includes what is indented but it is recommended to leave
# 2 lines of space after the last line of method.
print(type(get_greeting("John")))
greeting1= get_greeting("John")
print("Type of greeting is",type(greeting1))
print(greeting1)

print(get_greeting("Yusuf"))
print(get_greeting("Sofi"))
print(get_greeting("Stevie"))

# create a method to find sum of given two integers.
# given means the method will take it as parameter.
# add an if statement in this method so it will prinrt error
# # if type of num1 or type of num2 is not float or integer.
# def sum(num1,num2):
#     return num1+num2
# print(type(sum(1,3)))
# print()

def sum(num1,num2):
    addition= num1+num2
    s    = str(type(addition))
    if "int" in s or "float" in s:
        return addition
    else:
        return"an error occured."

print(sum("A","B"))
print(sum(1,3))
# Methods will always stop when the code reachs the return statment.


def sum2(*nums):
    sum=0
    for element in nums:
        sum += element
    return sum


print(sum2(1,5,6,8,9))