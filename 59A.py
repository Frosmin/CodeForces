

# También puedes usar en una palabra
palabra = input()
mayusculas = 0
minusculas = 0
for caracter in palabra:
    if caracter.isupper():
        mayusculas +=1
    elif caracter.islower():
        minusculas +=1
if mayusculas <= minusculas:
    print(palabra.lower())
else:
    print(palabra.upper())