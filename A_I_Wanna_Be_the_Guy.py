


n  = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
a[0] = a[1]
b[0] =b[1]
nueva_lista= set(a+b)

print("I become the guy." if len(nueva_lista) == n else "Oh, my keyboard!")