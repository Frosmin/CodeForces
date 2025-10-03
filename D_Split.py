from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    
    total = Counter(a)
    
   
    posible = True
    for valor, count in total.items():
        if count % k != 0:
            posible = False
            break
    
    if not posible:
        print(0)
        continue
    

    max_permitido = {}
    for valor, count in total.items():
        max_permitido[valor] = count // k
    
    contador = 0
    

    for l in range(n):
        freq = Counter()
        
        for r in range(l, n):
            freq[a[r]] += 1
            

            valido = True
            for valor, count in freq.items():
                if count > max_permitido[valor]:
                    valido = False
                    break
            
            if valido:
                contador += 1
    
    print(contador)