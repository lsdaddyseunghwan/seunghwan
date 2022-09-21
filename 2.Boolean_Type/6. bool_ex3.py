# veera wants lose 10 pounds in one month.
# there are multiple conditions to lose 10 pounds in a month.
# veera needs to walke 10000 steps daily or need to run at least 4 miles a day.
# and addition to those, veera needs to eat less than 1500 calories daily.
# we should create a program to calculate if veera can loose weight or not.

from multiprocessing.connection import wait


walking_steps =7000
running_distance= 0.2
daily_calory= 1200

can_loose_weight= (walking_steps >= 10000 or running_distance >= 4) and daily_calory < 1500

print("veera can loose weight", can_loose_weight)


