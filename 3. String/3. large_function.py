
# len() function allows us to learn how many characters used to create string.
#$ length function counts spaces as well.

str= "Techtorial"
str1= "Techtorial "

print(len(str)) #10

print(len(str1)) # 11

# length function will return an integer value so we can assign integer variables using
# length function

legnth_of_the_str = len(str)

print(legnth_of_the_str)  # 10
print(type(legnth_of_the_str)) # class 'int'

# create a program to print True if the length of str is even number
# Even number can be divided by 2

is_length_even = legnth_of_the_str % 2 == 0



print(is_length_even) # True







