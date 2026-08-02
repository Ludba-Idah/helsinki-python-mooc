def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def shape(size, shape1, height, shape2):

    i = size
    s = 0
    while 0 <= i:
        line(s, shape1)
        i-=1
        s += 1
    
    i = 0
    while i < height:
        line(size, shape2)
        i += 1
 
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")