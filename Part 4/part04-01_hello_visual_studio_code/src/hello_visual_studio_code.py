Editor = input ("Editor: ")

while True:
    Editor = Editor.lower()
    if Editor != "visual studio code":
        if Editor == "word" or Editor == "notepad":
            print("awful")
        elif Editor == "":
            continue
        else:
            print("not good")
    else:
        print("an excellent choice!")
        break
    Editor = input ("Editor: ")