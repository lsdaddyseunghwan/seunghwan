# str="New Name"
# print(str.endswith("Name"))   # True




full_names=[]
emails=[]

for i in range(10):
    print("Enter a full name")
    f_name=input()
    full_names.append(f_name)
    f_name=f_name.replace(" ","").lower()+"@gmail.com"
    emails.append(f_name)

print(full_names)
print(emails)
