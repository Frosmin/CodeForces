def repeticion (x,y):
    prod = 0
    while y!=0:
        prod += x
        y -=1
    return prod

print(repeticion(5,2))