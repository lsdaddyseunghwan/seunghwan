# fruits=("strawberry","apple","orange","banana","orange")

# print(fruits)

# print(type(fruits))  # <class 'tuple'>

# print(fruits.index("apple")) # -> 1

# print(fruits.count("orange")) # -> 2


# # Accesing the elements of a tuple

# # we can use index numbers as we did with list.
# # getting the third element from tuple
# print(fruits[2])

# print(fruits[0])

# # using for loop with tuples.

# for element in fruits:
#     print(element)

# # fruits=("strawberry","apple","orange","banana","orange")

# # from this tuple print out first fruit name
# # that has odd length. If there is no fruit with
# # odd length pring odd length coundn't be found.

fruits=("strawberry","apple","orange","banana","orange")


# mine________________________________________________________
# print(fruits)
# element=list(fruits)
# for element in fruits:
#     if len(fruits) % 2 !=0:
#         print("element is odd length")
#     else:
#         print("element is even")
#_____________________________________________________________

# I have to check length of each fruits until i encounter a
#  odd one.

for fruit in fruits:
    if len(fruit) % 2 !=0:
        # I have found odd length
        odd_fruit= fruit
        break      
if odd_fruit !="":
    print("First odd fruit is",odd_fruit)
else:
    print("Odd length fruit is not found.")


