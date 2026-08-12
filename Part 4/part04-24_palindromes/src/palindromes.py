def palindromes(word):
    return word == word[::-1]

while True:
    string = input("Please type in a palindrome: ")
    
    if string == "":
        continue
        
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break
    
    print("that wasn't a palindrome")