def rCountTo30(a, b, c, d):
    if a * 4 + b * 5 + c * 6 > d:
        return False

    elif a * 4 + b * 5 + c * 6 == d:
        return True

    else:
        if rCountTo30(a + 1, b, c, d) or rCountTo30(a, b + 1, c, d) or rCountTo30(a, b, c + 1, d):
            return True

        else:
            return False


print(rCountTo30(0, 0, 0, 11))