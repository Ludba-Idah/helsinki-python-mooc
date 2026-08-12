def invert(dictionary: dict):

    temp_items = []
    
    for key, value in dictionary.items():
        temp_items.append((value, key))
    
    dictionary.clear()
    
    for value, key in temp_items:
        dictionary[value] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)