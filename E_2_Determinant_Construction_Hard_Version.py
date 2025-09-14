import math
def attempt(x,y):
    matriz = [[0] * 50 for _ in range(50)]
    n = 50
    while(1):
        if(x > y):
            matriz[n-1][n-1] = 1
            matriz[n-1][n-2] = 1
            matriz[n-2][n-1] = -1
            x, y = y, x-y
        elif(x < y):
            if(y - x < x):
                matriz[n-1][n-1] = 0
                matriz[n-1][n-2] = 1
                matriz[n-2][n-1] = -1
                x, y = y, x
            else:
                matriz[n-1][n-1] = 1
                matriz[n-1][n-2] = 1
                matriz[n-2][n-1] = 1
                x, y = y, y-x
        elif(x == 1):
            for i in range(n):
                matriz[i][i] = 1
            break
        else:
            matriz[n-1][n-1] = 1
            y = math.floor(x * ((5 ** 0.5) - 1) / 2 + 0.5)
        if(n < 2):
            return [-1]
        n -= 1
    return matriz
for _ in range(int(input())):
    x = int(input())
    y = (1 if x==1 else math.floor(x * ((5 ** 0.5) - 1) / 2 + 0.5))
    matriz = [-1]
    while(len(matriz) == 1):
        matriz = attempt(x, y)
        y += 1
    print(50)
    print("\n".join([" ".join([str(j) for j in i]) for i in matriz]))