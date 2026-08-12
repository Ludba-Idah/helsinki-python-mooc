word_list = []
num = 0

while True:
    word = input("Word: ")

    if word in word_list:
        break
    else:
        word_list.append(word)
        num += 1
print(f"You typed in {num} different words")