# Using the input function asks the user to input the min and
# max number. Write a python code that will calculate the sum
# of numbers between the range of min and max and those that
# can only be divided by 3 and 11. 
# (min and max numbers are included)
# Example: 
# 0, 99 -> 33 + 66 + 99 = 198

# print("Enter a max number")
# max=int(input)
# print("Enter a min number")
# min=int(input)


# num=range(0,9)
# num=1
# while True:
#     if num %3==0:
#         print("num is divisible by 3")
#         num+=1
#     elif num % 11==0:
#         print("num is divisible by 11")   
#     else:
#         break

# print(num)    


# for index in range(3,7):
#     if list[index] % 3 !=0:
#         print(list[index])

#     elif list[index] % 11 !=0

s  = {0}
s2 = {99}
print(min(s))
print (max(s2))

min = 0
max1 = 99
#In the first iteration of the loop i should 
# change the value of the min but later on I should only change 
# it when the min is bigger than the number
# in the loop below how can I understan it is the first iteration
count_of_iteration = 0
for number in s:
    if count_of_iteration == 0:
        min = number
        max1 = number
    if number < min:
        #If code comes to this line it means min is bigger than number
        min = number
    elif number > max1:
        max1 = number    
    count_of_iteration+=1  
   


print("This is the min from the second first set",min)
print(max1)


max =0
for number in s2:
    if max == 0:
        max = number
    if max < number:
        max = number

print ("This is the maximum from the second set",max)    

print("Multiplication of min and max is", min*max)