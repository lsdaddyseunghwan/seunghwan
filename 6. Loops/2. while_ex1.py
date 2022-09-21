
# ask suer to give u a string
# from that string print index numbers of all the e's

print("enter text")
str=input()

# we can access string elements using their indexes.
index= 0
# index number is always smaller than length of the string.
# "example"
#  0123456 index numbers
#  1234567 length numbers
length_of_str= len(str)

while index < length_of_str:
    # I want to acces the element with index number str[index]
    if str[index] == "e":
        print(f"Index number of e is {index}")
    index +=1
    




















