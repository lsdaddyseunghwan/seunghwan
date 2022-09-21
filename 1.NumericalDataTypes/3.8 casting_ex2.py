


# find the numerical sum of "4.3" and '4'in float
# find the multiplication of "5" and '3'in float
# find the "12" divided by '3' and convert it to in integer data type.


# my answer
a=4.3
b=4
c=5
d=3
e=12
f=3

result1= float(a) + float(b)
result2= float(c*b)
result3= int(e/f)

print("result 1 is", result1)  # 8.3
print("result2 is ", result2)  #20.0
print("result3 is", result3)   # 4


# teacher answer

num1= "4.3"
num2= '4'
result1= float(num1) + float(num2)
print("result 1 is", result1)  #8.3
#-----------------------------------------

num3= "5"
num4= '3'
result2=float(num3)*float(num4)
print("result2 is",result2)    # 15.0
#---------------------------------------------------

num5= "12"
num6= '3'
result3= int(int(num5)/ int(num6))  
print("type of result3 is", type(result3))
print("the result 3 is equal to", result3) #4

# result 3 is equal to 4