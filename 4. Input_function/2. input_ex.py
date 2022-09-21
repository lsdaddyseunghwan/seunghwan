
#user want to deposit his money in to his account
# he already has $ 200 in his account
# he has three different paychecks (400, 600, and 350)
# he can only deposit one paycheck at a time
# after he deposit all the money in the account
# he bough a phone for $ 599, and headphone for $ 299
# create a python program to calculate his final money in the account.
# use input fuction to get all the value.

bank_acct=200

print("please enter the first paycheck amount you want to deposit")

first_deposit= int(input())

bank_acct+=first_deposit

print("please enter the second paycheck amount you want to deposit")
second_deposit= int(input())

bank_acct += second_deposit

print("please enter the third paycheck amount you want to deposit")

third_deposit= int(input())

bank_acct+= third_deposit

print("please enter the dollar amount of phone you want to buy")
phone=int(input())
bank_acct-=phone

print("please enter the dollar amount of headphone you want to buy")
head_phone=int(input())
bank_acct-=head_phone

print("His final money in the bank account is",bank_acct)