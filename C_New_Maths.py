# def multi(lista,num):  
#     i = 1
#     res = 0
#     for numero in reversed(lista):
#         residuo = ((numero*num)%10)*i
#         res += residuo
#         i=i*10
#     return res


# def suma_sin_acarreo(a, b):

#     a_str = str(a)
#     b_str = str(b)
    
#     max_len = max(len(a_str), len(b_str))
#     a_str = a_str.zfill(max_len)
#     b_str = b_str.zfill(max_len)
    
#     resultado = ""
#     for digito_a, digito_b in zip(a_str, b_str):
#         suma = int(digito_a) + int(digito_b)
#         resultado += str(suma % 10)  
    
#     return int(resultado)


# def suma_lista_sin_acarreo(lista):
#     resultado = 0
#     for numero in lista:
#         resultado = suma_sin_acarreo(resultado, numero)
#     return resultado
        



# def suma_listas_de_digitos_sin_acarreo(listas):
#     max_len = max(len(l) for l in listas)
#     # Rellenar con ceros a la izquierda
#     listas = [[0]*(max_len - len(l)) + l for l in listas]
#     resultado = []
#     for digitos in zip(*listas):
#         resultado.append(sum(digitos) % 10)
#     return resultado
  
    
# import math  

# n = int(input())

# i = math.ceil(n**0.5)

# while i < n:
#     lista = [int(digito) for digito in str(i)]
#     resultados = []
#     j = 0
#     for item in reversed(lista):
#         resultado = multi(lista, item)*10**j
#         resultado = [int(digito) for digito in str(resultado)]
#         resultados.append(resultado)
#         j+=1
#     numerito = (suma_listas_de_digitos_sin_acarreo(resultados))
#     numero = int(''.join(map(str, numerito)))

#     if numero == n:
#         print(i)
#         exit()

#     i+=1
# print(-1)



def dfs(x,f):
        if f:
            return
        if x == L + 1:
            f = True

            result = ''.join(str(a[i]) for i in range(1, n + 1))
            print(result)
            exit()
            return
        
        for d in range(10):
            tp = 0
            a[x] = d
            if x > n and d:
                return
            for j in range(1, x + 1):
                if x - j + 1 > n:
                    continue
                if j > n:
                    continue
                tp += mp[a[j]][a[x - j + 1]]
                tp %= 10
            
            if tp == p[x]:
                dfs(x + 1,f)
        
  

    
    
    
mp = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        mp[i][j] = (i * j) % 10
        
s = input()
L = len(s)
n = (L + 1) // 2  



p = [0] * (L + 1)
for i in range(1, L + 1):
    p[i] = int(s[i - 1])



a = [0] * (L + 1)  
f = False  
    

    
dfs(1,f)  
    
if not f:
    print(-1)