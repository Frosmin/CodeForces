import sys
from collections import deque

n = int(sys.stdin.readline())  

valores_cadena = sys.stdin.readline().split()  
variables = {}

for i in range(n):
    codigo_caracter = ord('A') + i  
    caracter_variable = chr(codigo_caracter)  
    variables[caracter_variable] = (valores_cadena[i] == 'T')



    
expresion = sys.stdin.readline().split()  
pila =  deque()
for token in expresion:
    if 'A' <= token <= 'Z':
        pila.append(variables[token])
    else:
        if token == '*':  
            op2 = pila.pop()  
            op1 = pila.pop()  
            pila.append(op1 and op2)
        elif token == '+':  
            op2 = pila.pop()
            op1 = pila.pop()
            pila.append(op1 or op2)
        elif token == '-':  
            op1 = pila.pop()
            pila.append(not op1)


resultado = pila[0]  
if resultado:
    print('T')
else:
    print('F')