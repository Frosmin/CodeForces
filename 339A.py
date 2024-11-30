def eliminar(lista):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == "+":
            lista.pop(i)
    return list(map(int,lista))



def main():
    try:
        lista = list(map(str, input().strip()))
        if not (1 <= len(lista) <= 100):
            raise ValueError("error")
        
        lista2 = eliminar(lista)
        listaOredenada = sorted(lista2)
        print("+".join(map(str, listaOredenada)))
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()