def number_analyzer():
    number = int(input("Enter the number: "))
    bigNum = []
    smallNum = []

    sNum = str(number)
    listNum = list(sNum)

    bigNum = sorted(listNum)
    smallNum = sorted(listNum, reverse=True)

    # print(bigNum)
    # print(smallNum)

    N1 = int("".join(bigNum))
    N2 = int("".join(smallNum))

    print(f"The value of subtraction of {N1} & {N2} is: ", N2 - N1)
    return


number_analyzer()
