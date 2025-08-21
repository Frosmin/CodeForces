def espacios(amigo,h):
    if amigo > h :
        return 2
    else :
        return 1



n,h = map(int, input().split())
amigos = list(map(int, input().split()[:n]))
res = 0
for amigo in amigos:
    if amigo > h:
        res += 2
    else:
        res +=1
print(res)