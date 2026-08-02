def mean(my_list):

    total = sum(my_list)
    count = len(my_list)
    return total / count

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    print(mean(my_list))

    my_list = [1, 2, 3, 4, 5]
    print(mean(my_list))