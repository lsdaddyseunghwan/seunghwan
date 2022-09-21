
# ask user to give two string values and
# print True if the second string starts with last two characters
# of the first string 
# or print True if the
print("please enter first string")
s1= input()

print("please enter second string")
s2=input()

last_two_ch_s1= s1[-2:]

is_second_start = s2.startswith(last_two_ch_s1)

first_two_ch_s2= s2[:2]

is_first_start= s1.startswith(first_two_ch_s2)

print(is_second_start or is_first_start)

