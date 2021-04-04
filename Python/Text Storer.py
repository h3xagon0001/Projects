def txtStorer():
    file = open("Text Storer.txt", "a")
    textToAdd = str(input("What would you like to add:"))
    file.write(textToAdd + "\n")
    file.close()

txtStorer()