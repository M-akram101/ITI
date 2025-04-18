def Invert(word1, word2):
    word1.sort()
    word2.sort()

    word1.split("")
    word2.split("")
    long = 0
    extra = ""

    if len(word1) > len(word2):
        long = len(word1)
    else:
        long = len(word2)

    for index in range(long):
        if word1[index] == word2[index]:
            continue
        else:
            extra = word1[index]


Invert("ceasar", "sceasra")
