# ask user to enter an integer number and print
# print out all the divisors of given integer number
# 6 -> divisors of six 1,2,3,6
# 10 -> 1,2,5,10
# 14 -> 1,2,7,14
# 11 -> 1,11

# possible divisers of given number.
# starts from 1 -> end at the given number itself 

print("Enter a number")
num= int(input())

possible_divisor=1
s=""
while possible_divisor <=num :
    # since we have the possible divisor, but we are not sure
    # if we can divide the number or not.
    # how can I understand if possible_divisor is an actual divisor or the number?
    # is an actual divisor of the number
    if num % possible_divisor == 0:
        s+= str(possible_divisor)+", "
    possible_divisor+=1
# remove suffix only removes if the string is ending with given characters.
print(s.removesuffix(", "),"are the divisors of the number")
# I want to print all divisors in one line like following example
# "1,2,3,6 are divisors of the number"


