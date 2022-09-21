nums= [ 1,2,3,1,2,3,4]

# remove all the number 2's from this list.

# for number in nums:
#     if number == 2:
#         nums.remove(number)

# print(nums) # it will remove all 2


# I can apply the remove method count times.

count=0
for number in nums:
    if number ==2:
        count+=1
print(count)

# I need to apply the remove method count times.
# # I need to create a loop that interates count times.

# If the count is 5
# range(count) 0 1 2 3 4

for i in range(count):
    nums.remove(2)
print(nums)

nums= [1,2,3,1,2,3,4,2,2,2]
# remove all the number 2's from this list.
# I can create a copy of this list

newList=nums.copy()

for number in newList:
    if number ==2:
        nums.remove(2)
print(nums)

