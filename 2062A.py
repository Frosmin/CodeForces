
def contador_unos(t):
    cont = 0
    for i in range(0, len(t)):
        if t[i] == "1":
            cont += 1
    return cont



n = int(input())
for i in range(n):
    cont = 0
    t = list(map(str ,input()))
    for j in range (0, len(t)-2):
        if t[j] == "1" and t[j+1] == "0" and t[j+2] == "1":
            t[j] = "0"
            t[j+1] = "1"
            t[j+2] = "0"
            cont+=1
        print(t)
    print(contador_unos(t)+cont)




