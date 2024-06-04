def factorial(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    for i in range(2, n+1):
        fact *= i
    return fact


def approx_sin(x, n):
    result = 0
    for i in range(n):
        values = (pow((-1), i) * pow(x, (2*i + 1))) / factorial(2*i + 1)
        result += values
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        values = (pow((-1), i) * pow(x, (2*i))) / factorial(2*i)
        result += values
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        values = pow(x, (2*i + 1)) / factorial(2*i + 1)
        result += values
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        values = pow(x, (2*i)) / factorial(2*i)
        result += values
    return result


x = float(input('x= '))
n = int(input('n= '))

print(approx_sin(x, n))
print(approx_cos(x, n))
print(approx_sinh(x, n))
print(approx_cosh(x, n))
