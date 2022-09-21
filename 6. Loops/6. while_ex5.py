# ask user to enter an integer number
# and print multiplication table for given number

# 3*1=3
# 3*2= 6



print("Enter a number")
num= int(input())

table_num = 1
while table_num<11:
    print(f"{num}*{table_num}={num*table_num}")
    table_num+=1
    