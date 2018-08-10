import math

def pascalTriangle(n):
    line = ''
    if n == 0:
        return '1'.center(5) + line
    else:
        for i in range(0, n + 1):
            line = line + (str(binomialCoefficent(n, i))).center(5) + ' '
        return pascalTriangle(n - 1) + '\n' + line


def binomialCoefficent(n, r):
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


print(pascalTriangle(4))
