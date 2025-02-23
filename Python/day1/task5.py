def palindrome_check():
    word = input("Enter a word: ")
    wordInverted = word[::-1]

    # print(word)
    # print(wordInverted)
    if word == wordInverted:
        print("PALINDROME!!")
        return
    print("NOT A PALINDROME!")


palindrome_check()
