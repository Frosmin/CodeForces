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
        



def suma_listas_de_digitos_sin_acarreo(listas):
    max_len = max(len(l) for l in listas)
    # Rellenar con ceros a la izquierda
    listas = [[0]*(max_len - len(l)) + l for l in listas]
    resultado = []
    for digitos in zip(*listas):
        resultado.append(sum(digitos) % 10)
    return resultado
  
    
import math  

n = int(input())

i = math.ceil(n**0.5)

while i < n:
    lista = [int(digito) for digito in str(i)]
    resultados = []
    j = 0
    for item in reversed(lista):
        resultado = multi(lista, item)*10**j
        resultado = [int(digito) for digito in str(resultado)]
        resultados.append(resultado)
        j+=1
    numerito = (suma_listas_de_digitos_sin_acarreo(resultados))
    numero = int(''.join(map(str, numerito)))

    if numero == n:
        print(i)
        exit()

    i+=1
print(-1)
        
        