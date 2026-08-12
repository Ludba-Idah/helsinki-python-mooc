def shortest(my_list):

    shortest = "LUDBAAA IDADAHHH"

    for string in my_list:
        if len(string) < len(shortest):
            shortest = string

    return shortest
           
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)