def numbers_generator():
    length = int(input("Enter the length of the word: "))
    start = int(input("Enter the number you want to start from: "))
    array = [0] * length
    array[0] = start

    for index in range(1, length):

        array[index] = array[index - 1] + 1

    print("Your array of nums equal: ", array)


numbers_generator()
