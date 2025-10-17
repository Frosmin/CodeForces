n,salto = map(int,input().split())
posicion = 1
vistos = 0
for _ in range(n):
    inicio,finn= map(int,input().split())
    distancia = inicio - posicion
    numero_saltos = distancia//salto
    vistos += inicio-((numero_saltos*salto)+posicion)
    vistos += finn-inicio+1
    posicion = finn+1

print(vistos)


