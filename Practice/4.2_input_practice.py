
#user want to deposit his money in to his account
# he already has $ 200 in his account
# he has three different paychecks (400, 600, and 350)
# he can only deposit one paycheck at a time
# after he deposit all the money in the account
# he bough a phone for $ 599, and headphone for $ 299
# create a python program to calculate his final money in the account.
# use input fuction to get all the value.

bank_account=200
paycheck_1=400
paycheck_2=600
paycheck_3=350
phone=599
headphone=299

bank_account_after_p1= bank_account+paycheck_1
bank_account_after_p2= bank_account+paycheck_2
bank_account_after_p3= bank_account+paycheck_3
bank_account_after_buying_a_phone=bank_account_after_p3-phone
bank_account_after_buying_a_headphone=bank_account_after_p3-headphone
money_in_the_account=bank_account_after_buying_a_headphone


print("$",money_in_the_account,"in the account")



