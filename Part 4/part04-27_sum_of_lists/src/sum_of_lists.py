def list_sum(a, b):

    new_list = []
    length = len(a)

    for i in range(length):
        new_list.append(a[i] + b[i])

    return new_list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))