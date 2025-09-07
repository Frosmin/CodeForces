def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(mcd(6,10))