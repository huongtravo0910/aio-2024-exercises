import math


def is_number(n):
    try:
        float(n)  # Type-casting the string to ‘float‘.
        # If string is not a valid ‘float‘,
        # it’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def activation_func():
    x = input('Input x = ')
    type_of_activation_function = input(
        'Input activation Function (sigmoid|relu|elu): ')
    if not is_number(x):
        print("x must be a number")

    x = float(x)

    result = 0

    if (type_of_activation_function == "sigmoid"):
        result = 1/(1 + math.exp(-x))

    if (type_of_activation_function == "relu"):
        if (x <= 0):
            result = 0
        else:
            result = x

    if (type_of_activation_function == "elu"):
        if (x <= 0):
            result = 0.01*(math.exp(x)-1)
        else:
            result = x

    print(f'{type_of_activation_function}: f({x}) = {result}')


activation_func()
