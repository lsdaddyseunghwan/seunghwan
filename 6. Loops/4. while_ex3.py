
# you have 40 dollar in the account.

acct, each_call= 40,5
call_number=1
while acct>= each_call:
    print(f"{call_number}th call is made")
    call_number +=1
    acct=acct-each_call
    print(f"after the call i have ${acct} left")




# My answer  문제점을 찾아라.ㅋㅋ 
#rint("enter number_of_call")
#number_of_call=input()
#phone_acct=40
#phone_charge=5
#while phone_acct >=number_of_call*phone_charge:
#    print(f"left money in the acct after each call {phone_acct}")
#    phone_charge+=5
