def longest(strings: list):

    longest_string = " "

    for current_string in strings:

        if len(current_string) > len(longest_string):
            longest_string = current_string

    return longest_string






if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))