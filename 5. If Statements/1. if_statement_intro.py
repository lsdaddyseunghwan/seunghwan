
num1= 5
num2= 8

if num1< num2 :
    print(f"{num1} is less than {num2}")

if num2<num1 :
    print(f"{num2} is less than {num1}") # this line will not get printed

# if statement will execute the next line only when the given condition is
# True.

is_num2_bigger =num2> num1

if is_num2_bigger:
    print("num2 is bigger than num1")

# ask user to enter a string

print("enter a string")
str=input()
is_lower =str.islower()

if is_lower:
    print("you entered correct cases") # line1
    print("because you enter all lower") # line2
print("you entered a string ")      # line3  # line3 not include if method
#                                            # so always printed

# line number1,2 is inside the if statement so they depend on condition, but
# line number3 is outside the if statement{ because no indentation} therefore,
# line number3 doesn't depend on any condition.


