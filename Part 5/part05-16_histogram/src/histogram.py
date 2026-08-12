def histogram(w:str):

    d = {}

    for letter in w:

        if letter not in d:
             
            d[letter] = ""
        d[letter] += "*"
        
    for letter, stars in d.items():

        print(f"{letter} {stars}")


if __name__ == "__main__":
    print(histogram("statistically"))