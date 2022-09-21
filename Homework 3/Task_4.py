# Ask the user to enter one in number between 1 to 10 then, Write the
# program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question.
# Example:
# Input: 6
# Output:
# 666666
# 55555
# 4444
# 333
# 22
# 1

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print("\n")