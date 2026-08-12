normal_list = []
ordered_list = []


while True:
    new_item = int(input("New item: "))

    if new_item == 0:
        break

    normal_list.append(new_item)
    print("The list now:", normal_list)
    
    ordered_list = sorted(normal_list)
    print("The list in order:", ordered_list)

print("Bye!")