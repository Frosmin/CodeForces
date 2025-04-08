
import math
def es_primo(n):
    if n <= 1:
        return False 
    if n == 2:
        return True  
    if n % 2 == 0:
        return False 
    hasta = int(math.sqrt(n)) + 1
    for divisor in range(3, hasta, 2):   #:D
        if n % divisor == 0:
            return False  
    return True 

z = int(input())
for _ in range(z):
    n, k = map(int, input().split())  
    if k == 1:
        if es_primo(n):
            print("YES")  
        else:
            print("NO")  
    else:
        if n == 1 and k == 2:
            print("YES")
        else:
            print("NO")