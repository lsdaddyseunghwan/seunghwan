# For this problem ask user to enter three numbers.
#  Round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
# so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its
# rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return
# the sum of their rounded values.
# Ex:1
# Input1: 16
# Input2: 17
# Input3: 18
# Output→ 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10
# Ex:2
# Input1: 12
# Input2: 13
# Input3: 14
# Output→ 30
# Ex:3
# Input1: 6
# Input2: 4
# Input3: 4
# Output→ 10
print("enter 1st any int number")
n1=int(input())
rounded_ten1 = round(n1, -1)
print("enter 2nd any int number")
n2 =int(input())
rounded_ten2 = round(n2, -1)
print("enter 3rd any int number")
n3 =int(input())
rounded_ten3 = round(n3, -1)

print(rounded_ten1+rounded_ten2+rounded_ten3)

