# Using input function ask user to enter a song name.
#  1. Print the first charachter of given song name.
# 2. Print the last charachter of given song name.
# 3. Print the length of the given song name.
# 4. Print the index number of "k" in this song name. 
# 5. Print the charachter from an index number of 3.
# 6. Print the song name in upper case.
# 7. Print the song name in lower case.
# Example: 
# Input: Mockingbird
# Output:
# M
# d
# 10
# 3
# k
# MOCKINGBIRD
# mockingbird




print("Enter a song name")
song= input()

print(song[0])
print(len(song)-1)
print(len(song))
print(song[3])
print(song.upper())
print(song.lower())


 
