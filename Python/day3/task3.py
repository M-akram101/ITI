def Sum(*args):
    summation = 0
    for arg in args:
        summation += arg

    print(summation)


def Sub(n1, n2):
    if n1 == 0 or n2 == 0:
        raise ValueError("Subtracting zero from number")
    subtraction = n1 - n2
    print(subtraction)


def Div(n1, n2):
    if n1 == 0 or n2 == 0:
        raise ZeroDivisionError("Cant divide with a 0")
    division = n1 / n2
    print(division)


def Mul(n1, n2):
    if n1 == 0 or n2 == 0:
        raise ValueError("Multiply with a zero")
    Multiplication = n1 * n2
    print(Multiplication)
