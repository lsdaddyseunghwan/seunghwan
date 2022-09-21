# isalpha() method
# it only returns true when all character of the string is letters.

s="This is text"
print(s.isalpha())
# False  because there is space. only letters can be True.

s=s.replace(" ","")
print(s.isalpha())
# True because using replace method we removed all the spaces from string.

s=s.replace(" ","-"),s.isalpha()




s1= "777edsad23"

print(s1.isnumeric())

print(s1.isalnum())
# it will True
s2="string"
s3= "777777"
s4= "234dfgdfg"
s5= "asdgasdf123-"
print(s2.isalnum()) # True
print(s3.isalnum())  # True
print(s4.isalnum()) #  True

print(s2.isnumeric()) # false
print(s5.isalnum()) 