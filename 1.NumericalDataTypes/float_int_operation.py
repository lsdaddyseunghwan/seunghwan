## Every math operation between float and int data type 

# will result in float data type


floatNum = 3.0

intNum   = 5


print("Type of floatNum is",type(floatNum))

print("Type of intNum is", type(intNum))


addition = floatNum + intNum

print("Additon of float and int is",type(addition))


subtraction = intNum - floatNum

print("Subtraction between int and float is",type(subtraction))


multiplication = floatNum * intNum

print("Multiplication between int data type and float is",type(multiplication))


division = intNum / floatNum 

print("The division between float and int data type is ", type(division))


remainder = floatNum % intNum

print("The remainder between float and int data type is",type(remainder))


remainder2 = intNum % floatNum

print("The remainder between float and int data type is",type(remainder2))


int_division = floatNum // intNum

print("The integer symbol division result between float and integer is ",type(int_division))


square_of_float= floatNum * floatNum

print(type(square_of_float))