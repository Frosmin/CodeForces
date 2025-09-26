n= int(input())
for _ in range(n):
    num, veces = map(int, input().split())
    print(0 if veces%2==0 else num)
