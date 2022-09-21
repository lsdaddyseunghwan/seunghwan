# str= "any string"
# index=0
# # I am assuming all letters have the count 1 in the string
# is_unique= True
# while index <len(str)-1:
#     if str.count(str[index])>1:
#         # Since the count is bigger than 1 str[index] is duplicated
#         is_unique= False
#         break

#     index+=1





str="abcdefg"
index=0
is_unique=True
while index< len(str)-1:
    if str.count(str[index])>1:
        is_unique=False
        break
    index+=1
if is_unique:
    print("string consists of unique leteers")
else:
    print("string has duplicated letter.")

