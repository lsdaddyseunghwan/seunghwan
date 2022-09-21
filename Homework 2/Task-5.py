# Using an input function enter three different ingredients for the product
# on the same line. Then ask the user to enter any int number. Change the
# first letter of the ingredients starting from the entered number.
# (Ingredients should start with different letters. Please read the example
# carefully ) 
# Example 1:
# Please enter three ingredients with spaces:
# Milk Peanuts Butter
# Please enter the int number:
# 5
# The output is:
# 5ilk 6eanuts 7utter

# Example 2:
# Please enter three ingredients with spaces:
# Sugar Cocoa Oil
# Please enter the int number:
# 3
# The output is:
# 3ugar 4ocoa 5i

print("Please enter three ingridients with spaces:")
s=input()
s=s.split()
print(s)
s1=s[0]
s2=s[1]
s3=s[2]
print("Please enter a number:")
n=int(input())
print(s1,s2,s3)
f1=s1[0]
f2=s2[0]
f3=s3[0]
s1=str(n)+s1.removeprefix(f1)
n=n+1
s2=str(n)+s2.removeprefix(f2)
n=n+1
s3=str(n)+s3.removeprefix(f3)
print(s1,s2,s3)