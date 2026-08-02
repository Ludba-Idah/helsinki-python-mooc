def longest_series_of_neighbours(my_list):

    max_length = 1
    current_length = 1

    for neighbour in range(1, len(my_list)):

        if my_list[neighbour] - my_list[neighbour - 1] == 1 or my_list[neighbour] - my_list[neighbour - 1] == -1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1

    return max_length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list)) 
