def most_common_character(string):

    count = 0
    most_common = ""

    for character in string:
        current_count = string.count(character)

        if current_count > count:
            count = current_count
            most_common = character

    return most_common






if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))