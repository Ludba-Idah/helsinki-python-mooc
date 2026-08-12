def anagrams(string1, string2):

    alphabetical1 = sorted(string1)
    alphabetical2 = sorted(string2)

    if alphabetical1 == alphabetical2:
        return True
    else:
        return False



if __name__ == "__main__":
    anagrams("a", "a")
    print(anagrams("a", "a"))
    