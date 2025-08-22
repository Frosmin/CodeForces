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
