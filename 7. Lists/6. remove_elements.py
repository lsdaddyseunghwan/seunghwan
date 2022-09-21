list=[1,2,3,4]

list.pop(2)
print(list)

#-----------------------------------
list2=[1,2,3,4]

list2.pop(3) # 3 is the index number which is number 4

print(list2) #[1, 2, 3]

list2.remove(2)  # 2 is number in the list, not index number.

print(list2)# [1, 3]




# @@@@  pop=index number,  @@@@ remove= list number, element

nums=[1,2,3,4,5,4,5,6,7]

# it will remove the first 5 that exist in the list

nums.remove(5)

print(nums) #[1, 2, 3, 4, 4, 5, 6, 7]

