
s= "Python"
#   012345 index number
print(s.find('y')) # 1

print(s.find('o')) # 4

s1="Java Java"
#   012345678 index number
print(s1.find("a")) # 1

# When we use multiple characters in find method
# it finds that sequence and return the index of first character
print(s1.find("va")) # 2

print(s1.find("al")) #-1  ,   if can't find. it will show -1

print(s1.find("z")) # -1
# index of first a present in the string
print(s1.find("a")) # 1
#what if I want to find index of last a present in the string?

print(s1.count("a")) # 2 

print(s1.rfind("a")) # 3 because index of last a present in the string
# index of last a present in the string means same as highest index number of a

# I want to find index of second a present in the string a
# I can find the lowest index for a True
lowest_a= s1.find("v")
#" Java Java"[1:] -> va Java
s1_newVersion= s1[lowest_a+1:]
# "va Java"
index_of_second_a = s1_newVersion.find("J")+lowest_a+1

print(f"index of second v is (index_of_second_a)")

