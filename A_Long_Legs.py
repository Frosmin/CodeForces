def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    x,y = map(int,input().split())
    mejor = x+y

    for m in range(1, max(x, y) + 1):
        movimientos = (m - 1) + ((x + m - 1) // m) + ((y + m - 1) // m)
        mejor = min(mejor, movimientos)
        if m > max(x, y):
            break
    
    print(mejor)
  
