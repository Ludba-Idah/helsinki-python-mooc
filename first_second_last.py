def first_word(sentence):
    word = ""
    i = 0
    while i < len(sentence):
        if sentence[i] == " ":
            break
        else:
            word += sentence[i]
        i += 1
    return word

def second_word(sentence):
    i = 0
    while i < len(sentence):
        if sentence[i] == " ":
            break
        i += 1
    while i < len(sentence):
        if sentence[i] != " ":
            break
        i += 1
    word = ""
    while i < len(sentence):
        if sentence[i] == " ":
            break
        else:
            word += sentence[i]
        i += 1
    return word

def last_word(sentence):
    word = ""
    i = len(sentence) - 1
    while i >= 0:
        if sentence[i] != " ":
            break
        i -= 1
    while i >= 0:
        if sentence[i] == " ":
            break
        else:
            word = sentence[i] + word
        i -= 1
    return word

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))