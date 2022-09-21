
s= "Python"
print(s.islower())   #False    because, it returns True when the string has only lower case
# letters

print(s.lower().islower()) # True    because the lower method makes all letters in lower case

s.upper()  # using methods in string will not effect the original
#value of the string.

print(s.isupper()) # False



# ask user to enter their name in uppercase
# if they didn't enter in upper cases print false

print("Enter your first name in upper cases")

first_name=input()

print(first_name.isupper())



