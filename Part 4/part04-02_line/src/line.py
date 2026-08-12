def line(integer, string):
    if string == "":
        print("*" * integer)

    else:
        f=string[0]
        print(f * integer)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")