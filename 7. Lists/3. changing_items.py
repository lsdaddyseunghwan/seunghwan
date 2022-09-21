list=["Str",'str1',False,5]

list[0]=3

print(list)

# list is mutable object. changable

list[1:3]= [1,2,3,4,5]
print(list)


list.insert(1,1.5)

print(list)
