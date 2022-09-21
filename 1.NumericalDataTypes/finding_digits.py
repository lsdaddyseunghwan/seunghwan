
a= 234




last_digit=a % 10
print(last_digit)

a = 981

# find the multiplication of digits of the number a
# number a will always have three digit number.
# 2 * 3 * 4 = 24
# when we find remainder with 10, it will give us
# the last digit of the number
# when I divide the number by 10, it will remove the last digit


last_digit = a % 10
print(last_digit)
# Following line will remove the last digit of variable a
a= a // 10
middle_digit = a%10
a= a // 10
first_digit = a % 10
multiplication = last_digit * middle_digit * first_digit

print("Multiplication result of all digit is", multiplication)


#Integer division will give us only the integer part of division
# For example
# 21 / 5 is 4.20 but if I use integer divisionm operator
# 21// 5 is 4


b= 34
print(b//10) 

c= 67
print(c//10)

d=105
print(d//10)

e=1273
print(e//10)


#ex)
a=123
#last_digit= a %10   #3
#mddile_digit= a%10   # 2
# first_digit= a%10   # 1

# multiplication= last_digit*middle_digit* first_digit
# p
