import sys

n = int(input())
if n % 4 == 0 or n % 7 == 0:
    print("YES")
    exit()

n = str(n)
res = any(caracter != "7" and caracter != "4" for caracter in n)
print("YES" if not res else "NO")