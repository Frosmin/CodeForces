# print(10)

# a = [1,2,3,4,5,6,7,8,9]
# print(a)

# maximo comun multiplo
def mcd(a,b):
    if a == 0:
        return b
    return mcd(b%a,a)

#minimo comun multiplo
def mcm(a,b):
    hcf = mcd(a,b)
    return (a*b)//hcf


print(11%5)