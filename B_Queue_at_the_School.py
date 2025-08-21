def boys(fila, n, t):
    for _ in range(t):
        i = 0
        while i < n - 1:
            if fila[i] == 'B' and fila[i+1] == 'G':
                fila[i], fila[i+1] = fila[i+1], fila[i]
                i += 2  
            else:
                i += 1
    return fila
            


n, t = map(int, input().split())
fila = list(map(str,input()[:n]))
print(''.join(boys(fila,n,t)))