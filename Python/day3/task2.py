myCard = ["Mohamed", "Akram", "26", "SW"]


with open("myFile.txt", "a") as file:
    for info in myCard:
        file.write(info + "\n")


with open("myFile.txt", "r") as file:
    print(file.read())
