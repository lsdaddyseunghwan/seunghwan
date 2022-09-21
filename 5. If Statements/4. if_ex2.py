# ask user to enter a positive integer number
# check if the given number is within 2 of a multiple of 10.
# if it is within 2 of a multiple 10 print
# your number is within a multiple 10
# if not print your number didn't match the expected requirement.

# 10- 20- 30- 40- 50-> so on
# if the user gives 21-> your number is within 2 of a multiple 10
# if the user gives 43-> your number is within a multiple 10
# if the user gives 39-> your number is within 2 of a multiple 10
# We need to use remainder operator.

# if the given number remainder with 10 is less than equals to 2
# it means it is within 2 of a multiple 10
# 11 % 10  -> 1
# 22 % 10  -> 2
# 30 % 10  -> 0

# 9        -> 9
# 18       -> 8
# if the also given number remainder with 10 is bigger or equal to 8
# the given number is within 2 of a multiple 10

#            8 9 10 11 12 
#          38 39 40 41 42
print("Enter a positive integer number")
num= int(input())
remainder= num % 10

if remainder >= 8 or remainder <= 2:
    print("your number is within 2 of a multiple 10")
else:
    print("your number didn't match the expected requirement.")
