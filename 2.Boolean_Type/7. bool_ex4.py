
# create a program to print True if there is enough ticket for the NBA game
# we  will have two variables sold tickets and max capacity of the stadium.
# if stadium capacity is more than sold tickets we should print true and all the
# other case we should print False.

sold_tickets, max_capacity = 12000, 13000


is_there_more_ticket= sold_tickets <= max_capacity  # True

print("Is there ticket left in the NBA game", is_there_more_ticket, "becuase we sold", 
sold_tickets," we have max capacity of", max_capacity)






