i = 0
items = 2
list = []
num = 1

items = int(input("How many items: "))

while i < items:
    items_in_list = int(input(f"Item {num}: "))
    i += 1
    num += 1
    list.append(items_in_list)
    

print(list)

