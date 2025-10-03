for _ in range(int(input())):
    n, k, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    contador = 0
    

    for b in range(n):
        distintos = set()
        
        for c in range(b, n):

            distintos.add(a[c])
            

            longitud = c - b + 1
            

            if len(distintos) > k:
                break
            
            if len(distintos) == k and l <= longitud <= r:
                contador += 1
    
    print(contador)