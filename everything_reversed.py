def everything_reversed(strings_list):

    reversed_list = []  

    for string in strings_list:
        string = string[::-1]  
        reversed_list.append(string)

    reversed_list = reversed_list[::-1]
    return reversed_list




if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

    my_list = ["erom eno", "elpmaxe", "ereht", "iH"]
    new_list = everything_reversed(my_list)
    print(new_list)