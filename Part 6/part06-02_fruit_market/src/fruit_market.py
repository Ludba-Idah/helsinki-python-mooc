def read_fruits():

    with open("src/fruits.csv") as new_file:

        fruits = {}

        for row in new_file:

            row = row.strip()
            parts = row.split(";")     
            name = parts[0]

            price = float(parts[1])
            
            fruits[name] = price
            
    return fruits

if __name__ == "__main__":
    print(read_fruits())
