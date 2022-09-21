# Ask user to enter any string value using input function.
# Then, remove all the spaces (" ") from the given string. 
# After removing the spaces from the string, 
# if the string's length is odd print True, otherwise print False. 
# Example: 
# Input : I love coding
# Output: True
# Input : one two 
# Output: Fals







print("Please enter a text with spaces")
str = input()
str=str.replace(" ","")

is_length_odd= len(str) %2 !=0

print(is_length_odd)

# when even cases.
# is_length_even= len(str) % 2 ==0
# print(is_length_even)