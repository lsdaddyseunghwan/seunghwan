
# ask user to enter a string and pring a rotated let 2 version
# where the 2 characters moved to the end.
# 'Hello' -> 'lloHe'
# 'java' -> vaja'

print("enter a text")
s=input()

first_two=s[:2]
rest_of_string= s[2:]

s=rest_of_string + first_two
print(s)


