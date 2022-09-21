dollar = 5.22
dollar_amount = dollar * 100

quarter_value = 25
dime_value = 10
nickel_value = 5
penny = 1
            
count_of_q = int(dollar_amount // quarter_value )

print(int(count_of_q), "quarters") 
                          
remaining_exchange_after_q = dollar_amount % quarter_value

count_of_d = int(remaining_exchange_after_q // dime_value)
print(int(count_of_d) , "dimes")
remaining_exchange_after_d = remaining_exchange_after_q % dime_value
count_of_nickel = int(remaining_exchange_after_d // nickel_value)
print(int(count_of_nickel), "nickels")
remaining_after_nickel = remaining_exchange_after_d % nickel_value

count_of_pennies = int(remaining_after_nickel // penny)

print(int(count_of_pennies),"pennies")

print("$",dollar,"will make",count_of_q,"quarters",count_of_d,"dimes",count_of_nickel,"nickels and",count_of_pennies,"pennies")


