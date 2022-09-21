
bool1= True
bool2= False
bool3= True
# noit operator will make true condition false, false conditions true.


print(not bool3)  # False
print( not bool2) # True

print( bool2 and bool1) # True  since and condition requires both side to be
# true for returning true this line will print False.

print(bool2 or bool1) # True  if one of condition is True, or will return True.

print(bool2 or not bool1) # False b.c not operator will
# make the bool1's value false so False will result in False. 

print(not bool2 and bool1) #True
