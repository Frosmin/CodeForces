
def an(x, y, id, w, h, lista):
    if y == 0:
        lista[0].append((x, id))
        return 1
    elif x == w:
        lista[1].append((y, id))
        return 1
    elif y == h:
        lista[2].append((-x, id))
        return 1
    elif x == 0:
        lista[3].append((-y, id))
        return 1
    return 0



w, h = map(int, input().split())
n = int(input())
# 0: abajo, 1: derecha, 2: arriba, 3: izquierd

lista = [[] for _ in range(4)]

freq = [0] * n

for i in range(n):
    
    a, b, c, d = map(int, input().split())
    freq[i] += an(a, b, i, w, h, lista)
    freq[i] += an(c, d, i, w, h, lista)
    

a = []
for i in range(4):
    lista[i].sort()
    a.extend(lista[i])
    
st = []  
cnt = [0] * n 

for _, x_id in a:
    if freq[x_id] != 2:
        continue
        
    cnt[x_id] += 1
    if cnt[x_id] == 2:
        if not st or st[-1] != x_id:
            print("N")
            exit()
        st.pop() 
    else: 
        st.append(x_id) 
        

if not st:
    print("Y")
else:
    print("N")

