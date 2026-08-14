def largest():

    with open("src/numbers.txt") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))
            
    return max(numbers)

if __name__ == "__main__":
    result = largest()
    print(result)