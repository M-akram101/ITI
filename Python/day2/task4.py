phone_book_dict = {}
phone_book_dict1 = {}

length_dict = int(input("Enter the length of the dictionary: "))

for value in range(length_dict):
    key = input("Enter your name: ")
    value = input("Enter your phone number: ")
    phone_book_dict[key] = value

    key2 = input("Enter your name: ")
    value2 = input("Enter your phone number: ")
    phone_book_dict1[key2] = value2

phone_book_dict.update(phone_book_dict1)

print("Here is the Phone book", phone_book_dict)
