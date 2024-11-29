
def buscarColum(lista):
    for i in range(0, len(lista)):
        if lista[i] == 1:
            return i
        
def main():
    fila = 0
    col = 0
    try:
        entrada = ""
        for i in range(5):
            lista = list(map(int, input().strip().split()))
            
            if buscarColum(lista) == None:
                pass
            else:
                fila = i
                col = buscarColum(lista)
                return print(abs(2-fila) + abs(2-col))
          
    except ValueError as e:
        print(f"Error: {e}")
    
    
if __name__ == "__main__":
    main()