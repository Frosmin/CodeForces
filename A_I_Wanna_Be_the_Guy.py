


n  = int(input())

a = list(map(int,input().split()))[1:]
b = list(map(int,input().split()))[1:]

# if n > 1:
#     if len(a) > 1 and len(b)> 1:
#         a[0] = a[1]
#         b[0] =b[1]
# nueva_lista= set(a+b)
# else:
#     print("Oh, my keyboard!")
#     exit()



nueva_lista= set(a+b)
print("I become the guy." if len(nueva_lista) == n else "Oh, my keyboard!")