def num_check():
    number = int(input("Enter a number to check: "))
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        return
    elif number % 3 == 0:
        print("Fizz")
        return
    elif number % 5 == 0:
        print("Buzz")
        return


num_check()
