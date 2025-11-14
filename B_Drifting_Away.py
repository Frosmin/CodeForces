import collections

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    n = len(s)
    circulo_encontrado = False
    for i in range(n - 1):
        if (s[i] == '>' or s[i] == '*') and (s[i + 1] == '<' or s[i + 1] == '*'):
            circulo_encontrado = True
            break
    if circulo_encontrado:
        print(-1)
    else:
        pre_nodo = [[] for _ in range(n)]
        for i in range(n):
            if s[i] == '<':
                if i > 0:
                    pre_nodo[i].append(i - 1)
            elif s[i] == '>':
                if i < n - 1:
                    pre_nodo[i].append(i + 1)
            else:  # '*'
                if i > 0:
                    pre_nodo[i].append(i - 1)
                if i < n - 1:
                    pre_nodo[i].append(i + 1)
                    
        nodos_anteriores = [[] for _ in range(n)]
        for i in range(n):
            for j in pre_nodo[i]:
                nodos_anteriores[j].append(i)
                
        dp = [0] * n
        maximo = [0] * n
        num_dependenci = [0] * n
        for i in range(n):
            num_dependenci[i] = len(pre_nodo[i])
            
        q = collections.deque()
        for i in range(n):
            if num_dependenci[i] == 0:
                dp[i] = 1
                q.append(i)
                
        while q:
            j = q.popleft()
            for i in nodos_anteriores[j]:
                candidato = 1 + dp[j]
                if candidato > maximo[i]:
                    maximo[i] = candidato
                num_dependenci[i] -= 1
                if num_dependenci[i] == 0:
                    dp[i] = maximo[i]
                    q.append(i)
                    
        print(max(dp))