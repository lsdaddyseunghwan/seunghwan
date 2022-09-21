# Reverse a given String and print it, if they have space in the
# beginning and at the end then remove it.  Without using
# slicing [ : :-1]. Try doing with for loop or while loop. 
# Example:  " Job" -> "boJ" 
#  * " Happy " -> "yppaH" 
#  * "Sun " -> "nuS" 
#  * " Dream Job!" -> "!boJ maerD" 


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")