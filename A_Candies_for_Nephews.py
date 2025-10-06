n = int(input())
for _ in range(n):
    caramelos = int(input())
    residuo  = caramelos%3 
    if residuo != 0:
        aumentar  = 3-residuo
        print(aumentar)
    else:
        print(0)
    

