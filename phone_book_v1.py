phone_book = {}
command = 0

while True:
    command = input("command (1 search, 2 add, 3 quit): ")

    if command == "3":
        print("quitting...")
        break

    else:
        if command == "1":
            name = input("name: ")

            if name in phone_book:
                print(phone_book[name])

            else:
                print("no number")

        elif command == "2":
            name = input("name: ")
            number = input("number: ")
            phone_book[name] = number
            print("ok!")

        else:
            continue
