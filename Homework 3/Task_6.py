# Using a input function enter a sentence that is not separated by space and each
# word starts with upper case. Print given String as separated words with spaces.
# Example: 
# Given Value: "IWantToLearnJava"
# Output: I Want To Learn Java
# Example-2: 
# Given Value: "ItIsSunnyOutside"
# Output: It Is Sunny Outside



str="IWantTolearnJava"
letter=str
is_upper=letter.isupper()
for letter in str:
    if letter== "uppercase":
        is_unique=" "
        print(letter," ")
        str+=1
# else:
#     print(str)

# x=False
# str="python"
# for letter in str:
#     if letter =="t":
#         x=True
# print(x)
