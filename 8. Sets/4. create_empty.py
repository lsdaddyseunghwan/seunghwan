s=set()

print(type(s))  # <class 'set'>

s.add("new value")

print(s)  # {'new value'}

s={}
print(type(s))  # <class 'dict'>@@@@@@@empty set= dict

# using set() function we can convert lists in to set
# How we can remove the duplicates from ths list below?
list=["s","s",2,2,4,5,6,3,6,3,2]

set1=set(list)
print(set1)
print(type(set1)) # set



# @@@@@@@@@@@@@@@@@@@@set remove duplicate

# clear()
set1.clear()

print(set1)
print(type(set1))  # class 'set'>



# copy method
list = ["s","s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print("From line 31",set1)

set2 = set1.copy()
print(set1 == set2)
print("set 2 from line 35",set2)
print(type(set2)) # set