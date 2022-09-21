
str="hello"
str1="hello"
str2="heLlo"
#Equal equal sign is case sensitive, so if cases of the two string is different it will
# return false

print(str== str1)  # True
print(str==str2)    # False  bc midlle L is capital.

# we can reassign and change the strinmg values as we were able to do with other
# data types.

str2= "hello"
print(str2) # hello

# since we reassgin and change the value of the str2
# equal coprision between str2 and str will give the result as true

print(str2== str)

# concatenating the strings
# concetanation is adding mroe string to the existing string value
str2= str2 +"world"
print(str2) # hello world

# we can use concatenation even when we are creating the string variable first time

str3= "hello"+"world"
print(str3) # hello world

str4= str + str1

print(str4) # hellohello





