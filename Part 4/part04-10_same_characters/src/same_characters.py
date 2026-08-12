# Write your solution here
def same_chars(word, index1, index2):

    if len(word) <= index2:
        index2 = -1

    if len(word) < index1:
        index1 = -1

    if word[index1] == word[index2]:
        return True
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))