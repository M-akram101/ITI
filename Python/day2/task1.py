def check_num():
    number = int(input("Enter a number: "))
    if number >= -5 and number <= 5:
        return True
    return False


print(check_num())
