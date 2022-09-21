
# We can two methods to remove elements from the set.
# discard() method and remove() method.

# remove(valueOfTheObject)

set={3,5,7,9}

# I want to remove the number 7 from the set.

set.remove(7)
print(set)  # {9 , 3 ,5 } no order

# When the element needs to be removed does not exist in the set
# it will throw an error.

# set.remove(7)  # error 

# discard(valueOfTheObject) method

set.discard(3)
print(set)
# When the element needs to be removed does not exist in the set
# it will throw an error and it won't anything
set.discard(3)



