ejem1 = [1,2,3,4]
ejem1.insert(2,10) #inserta en al posicion,valor_que_se_inserta
ejem1.remove(1) # le das el elemento para borrar borra los 1 de la lista
print(ejem1)
elemento = ejem1.pop(1) #borra el incice de, tambien devuelve el elemento borrado 
print(ejem1) #borra el indice 
print(elemento)

ejem1.clear() #elimina todos los elementos de la lista
print(ejem1)


ejem2 = [1,2,3,4,5]
print(ejem2.index(2)) #devuelve el primer indice donde aparcere el valor señalado



nums = [1,2,3,4,5,6,7,8,9,10]
cuadrado = list(map(lambda x: x*x, nums))


print(list(range(10))) #del 0 al 9 dentro de una lista 

lista_cuadrados = [i**2 for i in range(10)]
print(lista_cuadrados)

n= 2
nueva_lista = [i for i in range(1,n+1)]


print(nueva_lista)



# El usuario introduce los números, por ejemplo: 10 20 10 30
lista = list(map(int, input().split()[:4]))

# 1. Convertimos la lista a un set para obtener solo los elementos únicos
# Para la lista [10, 20, 10, 30], el set será {10, 20, 30}
numeros_unicos = set(lista)

# 2. Calculamos la cantidad de números únicos
cantidad_unicos = len(numeros_unicos)

# 3. Imprimimos el resultado final
print(4 - cantidad_unicos)