lst = [1,2,3,4,5,6,7,8,9]  #la lista tiene que estar ordenada



def sorted_list_to_bst(sorted_lst):
    """
    Convierte una lista ordenada en un Árbol Binario de Búsqueda balanceado
    representado como una lista de adyacencia.
    """
    adj_list = {}
    if not sorted_lst:
        return adj_list, None

    def build_tree(start, end):
        """
        Función auxiliar recursiva para construir el árbol.
        Devuelve el valor del nodo raíz del subárbol construido.
        """
        if start > end:
            return None

        # Elige el elemento del medio como raíz
        mid = (start + end) // 2
        root_val = sorted_lst[mid]

        # Construye recursivamente los subárboles izquierdo y derecho
        left_child = build_tree(start, mid - 1)
        right_child = build_tree(mid + 1, end)

        # Guarda los hijos en la lista de adyacencia
        # El formato es: {nodo: [hijo_izquierdo, hijo_derecho]}
        adj_list[root_val] = [left_child, right_child]

        return root_val

    # Inicia la construcción del árbol y obtiene la raíz
    root = build_tree(0, len(sorted_lst) - 1)
    
    return adj_list, root

# Construye el árbol y obtén la lista de adyacencia y la raíz
bst_adj_list, root_node = sorted_list_to_bst(lst)

print(f"Lista original: {lst}")
print(f"Raíz del árbol: {root_node}")
print("Lista de adyacencia del BST:")
# Imprime el diccionario de forma ordenada para mejor visualización
for node in sorted(bst_adj_list.keys()):
    print(f"  {node}: {bst_adj_list[node]}")



    





