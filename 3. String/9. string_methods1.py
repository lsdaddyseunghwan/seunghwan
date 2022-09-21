

s= "Python"
print(s.upper())  # -> PYTHON

print(s)          # -> Python

# since the string is immutalbe, it will not change its value unless it is ressigned.

s= "PYthon"

print(s.lower())  # -> python

# Method chaining -> as long as the method you use in the string returns another
# string you can use other string methods

print(s.lower().upper())  # PYTHON it will be printed all upper case since
#                           it is the last method

print(s.upper().lower())   # python

print("result of swap case method",s.swapcase()) # pyTHON

print("result of capitalize method", s.capitalize()) # Python




