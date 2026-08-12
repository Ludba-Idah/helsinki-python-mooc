inp = "e"
list = []
num = 0

while inp != "x":
    print("The list is now", list)
    inp = input("a(d)d, (r)emove or e(x)it: ")

    if inp == "d":
        num += 1
        list.append(num)

    elif inp == "r":
        if len(list) > 0:
            num = list[-1] -1
            list.pop()
        else:
            continue
    elif inp == "x":
        break
print("Bye!")
 