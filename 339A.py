def eliminar(lista):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == "+":
            lista.pop(i)
    return list(map(int,lista))



def main():
    try:
        lista = list(map(str, input().strip()))
        print("+".join(sorted(lista)))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()