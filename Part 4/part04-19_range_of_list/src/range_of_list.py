def range_of_list(my_list):
    smallest = min(my_list)
    largest = max(my_list)
    return largest - smallest

if __name__ == "__main__":
    my_list = [3, 6, -4]
    print(range_of_list(my_list))