
# print numbers from 1 to 10 inclusive
num=1
while num <=10:
    print(num)
    # I have to update the value of variable num in the loop so
    # condition will become false eventually.
    num= num+ 1

num=2
    # print even numbers that are smaller eual to 10
while num <= 10:
    print(num)
    num=num+2
print(f"Value of the variable num is {num}") # 12

num=1
while num <=10:
    if num%2==0:  # this line is in the while loop
        print(num) # this line is in the whjle as well as in the if statement
    num+=1         # this line is in the while loop
print(num) # 11
# from 1 to 20 inclusive, print every odd number
# "this is an odd number{ value of number}"
# print every even number
# "this is an even number {value of number}"

num=1
while num <=20:
    #In the while loop I have to decide num is currently even or odd
    if num % 2==1:
        print(f"This is an odd number {num}")
    else:
        print(f"This is an even number{num}")
    num +=1 

num=0
while num < 1 :
    print("in the while loop")
print("outside thewhile after the infinite loop")


