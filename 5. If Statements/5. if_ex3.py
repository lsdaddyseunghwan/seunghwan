# ask user to give you two integer numbers.
# find the sum of these two integer numbers.
# if sum of these two integer is smaller than 10 
# print sum of these two number is 10
# if sum of these two number is between 10- 19 inclusive,
# print sum of these two numbers is 20
# for all other conditions
# print the actual sum of these two numbers.

print("plz enter a first number")
n1=int(input())

print("plz enter a second number")
n2=int(input())

sum= n1 + n2
if sum <10:
     print(" sum of these two number is 10")
elif sum>=10 and sum<= 19:
    print("sum of these two numbers is 20")
else:
    print(f"sum of these two numbers is {sum}")

    