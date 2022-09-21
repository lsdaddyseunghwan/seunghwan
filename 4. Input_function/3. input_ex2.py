
# ask user to give you a string
# ask user to give count order number of the letter and print that letter
# from the string

from platform import python_branch


print("Enter a text")
text= input()

print("Enter the order number of the letter you want to see")

order_number= int(input())
 
# we have to consider that user doesn't know aboout index numbers and
# the number user provided will be 1 bigger than the index number
# "python"
#  012345 (index number)
#  123456 (order number which user will think it is true.)

index_number= order_number-1

print(text[index_number])

