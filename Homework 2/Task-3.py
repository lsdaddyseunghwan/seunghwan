#Using the input function ask the user to enter one sentence with three
#words and print the index number of each word's last character and then
#print the sum of each index number that you found. 
#For Example: 
#Input: 
#"Importance of Human" --> it can be any three-word sentence. 
# Output: 
#9 --> index number of 'e'
#12 --> index number of 'f'
#18 --> index number of 'n'
#The sum: 39



# how can i find first index of space?
## using find(" ") we can find index of first space.
# -1

# second string-- we can use rfind(" ")

#last string   len(str)-1
print("enter one sentence with two spaces")
str=input()
last_index_of_firstword=str.find(" ")-1

last_index_of_secondword= str.rfind(" ")-1

last_index_of_lastword=  len(str)-1


print(last_index_of_firstword+last_index_of_secondword+last_index_of_lastword)
