# vowels = ['a','e','i','o','u','A','E','I','O','U']
# counter = 0
# index=0
# # word ="ytrer"
# def vowels(word):
#     for value in


def vowel_count():
    word = input("Please enter a word: ")
    counter = 0
    vowels = "aeiouAEIOU"
    for character in word:
        if character in vowels:
            counter += 1

    print(f"You have {counter} vowels in your word ")


vowel_count()
