def all_the_longest(my_list):
    maximum = []
    max_length = 0

    for string in my_list:

        if len(string) > max_length:
            max_length = len(string)
            maximum = [string]
            
        elif len(string) == max_length:
            maximum.append(string)

    return maximum

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)
