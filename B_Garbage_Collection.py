dia = lambda d,r ,q : d+ (r-d % q + q ) % q
lista_recojo = []
def recojo(d,q,r):
    print(dia(d,r,q))
    



n = int(input())
lista_tipos = []
for i in range(n):
    q,r = map(int,input().split())
    lista_tipos.append([q,r])
dias = []
q = int(input())
for i in range(q):
    t,d = map(int,input().split())
    dias.append([t,d])
for j in range(q):
    basura = dias[j]
    d = basura[1]
    tipo = basura[0]
    q = lista_tipos[tipo-1][0]
    r = lista_tipos[tipo-1][1]
    recojo(d,q,r)
    
    
