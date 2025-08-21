def espacios(amigo,h):
    if amigo > h :
        return 2
    else :
        return 1



n,h = map(int, input().split())
amigos = list(map(int, input().split()))
res = 0
for amigo in amigos:
    res += espacios(amigo,h) 
print(res)