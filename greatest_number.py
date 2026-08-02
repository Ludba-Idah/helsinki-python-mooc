def greatest_number(n1,n2,n3):
    number = 0
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    elif n3 >= n2:
        return n3
    
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(greatest_number(3, 5, 7))
