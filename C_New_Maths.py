def multi(lista,num):  
    i = 1
    res = 0
    for numero in reversed(lista):
        residuo = ((numero*num)%10)*i
        res += residuo
        i=i*10
    return res


def suma_sin_acarreo(a, b):

    a_str = str(a)
    b_str = str(b)
    
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    resultado = ""
    for digito_a, digito_b in zip(a_str, b_str):
        suma = int(digito_a) + int(digito_b)
        resultado += str(suma % 10)  
    
    return int(resultado)


def suma_lista_sin_acarreo(lista):
    resultado = 0
    for numero in lista:
        resultado = suma_sin_acarreo(resultado, numero)
    return resultado
        
    
  
    
    

n = int(input())

for i in range(1,n+1):
    lista = [int(digito) for digito in str(i)]
    resultados = []
    j = 0
    resultado = 0
    for item in reversed(lista):
        resultado = multi(lista, item)*10**j
        resultados.append(resultado)
        j+=1
    if suma_lista_sin_acarreo(resultados) == n:
        print(i)
        exit()
print(-1)
        
