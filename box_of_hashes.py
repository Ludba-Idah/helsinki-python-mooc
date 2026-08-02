def box_of_hashes(area):
    w = 10
    l = area
    def line():
        l = area
        w = 10

        while l > 0:
            ar = "#" * w
            print(ar)
            l-=1
    line()
        


if __name__ == "__main__":
    box_of_hashes(5)
    print ()
    box_of_hashes(202)
