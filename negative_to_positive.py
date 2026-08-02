pos_integer = int(input("Please type in a positive integer: "))
neg_integer = -pos_integer
for i in range(neg_integer, pos_integer + 1):
    if i == 0:
        continue
    
    print(i)
