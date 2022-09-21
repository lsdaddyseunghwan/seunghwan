
n = 24689
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)

#-------------------------------------

number="24689"
print(number[ : : -1])

#----------------------

number= 24689
number= str(number) 

print(number[::-1])