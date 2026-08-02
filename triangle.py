def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
 
def triangle(size):
    i = size
    s = 0
    while 0 <= i:
        line(s, "#")
        i-=1
        s += 1
 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
