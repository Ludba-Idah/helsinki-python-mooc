def create_tuple(x: int, y: int, z: int):

    list = [x, y, z]
    list.sort()

    answer = sum(list)

    return (list[0], list[2], answer)



if __name__ == "__main__":

    print(create_tuple(4, 7, 1))