def sum_of_positives(numbers):

    total = 0

    for num in numbers:
        if num > 0:
            total += num

    return total

if __name__ == "__main__":
    print(sum_of_positives([1, -2, 3, 4, -5]))