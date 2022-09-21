# Please use method chaining for the following Strings. Methods are
# provided next to the String.
# String “ Snicker " —> strip, upper, remove prefix and slice the string with
# any number of your choice
# String “Cookie” —> lower, replace ‘o’ with ‘u’, remove suffix e, 
# starts with ‘C’

s1=" Snicker "
#   012345678 index number
print(s1.strip().upper().removeprefix("S")[2:-2])


s2="Cookie"
#   012345 index

print(s2.lower().replace ("o","u").removesuffix("e").startswith("C"))





