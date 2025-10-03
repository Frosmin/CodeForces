def lista_a_bst_array(lista):
    """Convierte lista a BST usando arrays    binary seach tree"""
    n = len(lista)
    izq = [-1] * n
    der = [-1] * n
    valores = lista[:]
    
    # Construir BST balanceado 
    def construir(arr, inicio, fin, pos):
        if inicio > fin:
            return -1
        
        medio = (inicio + fin) // 2
        valores[pos] = arr[medio]
        
        if inicio <= medio - 1:
            izq[pos] = pos * 2 + 1
            construir(arr, inicio, medio - 1, izq[pos])
        
        if medio + 1 <= fin:
            der[pos] = pos * 2 + 2
            construir(arr, medio + 1, fin, der[pos])
        
        return pos
    
    lista_ordenada = sorted(lista)
    construir(lista_ordenada, 0, n - 1, 0)
    
    return izq, der, valores

def inorden_array(pos, izq, der, valores):
    if pos == -1 or pos >= len(valores):
        return
    inorden_array(izq[pos], izq, der, valores)
    print(valores[pos], end=" ")
    inorden_array(der[pos], izq, der, valores)


lista1 = [1,8,5,2,3,4,6]
arbol = lista_a_bst_array(lista1)

print(lista_a_bst_array(lista1))





