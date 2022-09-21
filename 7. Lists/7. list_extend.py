need = ["pencil","eraser","notebook"]
need2 = ["computer","mouse","keyboard","camera"]

need.extend(need2)

need2.clear()

print(need)

print(need2) # empty list



# extend method takes the copy of need2 list and adds it to need.
# later on chaning the value of need2 will not effect the need
# because when we are adding with extend method we didn't exactly
# uuse need2 we have used the copy of need2

