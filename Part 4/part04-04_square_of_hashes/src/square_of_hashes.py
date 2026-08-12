def square_of_hashes(size):
    lw=size
    t=lw
    def line():
        lw=size
        t=lw

        while t > 0:
            print("#" * lw)
            t-=1
    line()

if __name__ == "__main__":
    square_of_hashes(5)
