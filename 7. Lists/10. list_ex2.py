
# nums=[1,2,10,11,13,17,21,26]

# # from the given list find sum of all the even numbers
# sum=0


# for number in nums:
#     if number % 2 ==0:
#         sum+=number

# print("Sum of all the even numbers from list is",sum)

#--------------------------------------------------------------

nums=[1,2,10,11,13,17,21,26]
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  중요
# from the given list find sum of all the even numbers
sum_even=0
sum_odd=0

for number in nums:
    if number % 2 ==0:
        sum_even+=number
    else:
        sum_odd +=number

print(number) # the variable number will take ths last value.
print("Sum of all the even numbers from list is",sum_even)
print("sum of all the odd number is", sum_odd)
