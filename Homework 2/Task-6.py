# Write the program to get the string value from the specified position.
# First, ask the user to enter one String value. Then ask the user to the
# enter starting number and ending number. After that, print the value
# between the given starting and ending numbers. (Note: since the user
# does not know the python, the user starts counting from 1, and the
# ending number will be included)
# Example:
# Please enter the String value:
# Definition of Science
# Please enter the starting number:
# 2
# Please enter the ending number
# 5
# The output is:
# efin


print("Enter a text")
text=input()
print("Enter starting number")
start=int(input())
print("Enter ending numbers")
end=int(input())
cut=text [(start-1):end]
print(cut)