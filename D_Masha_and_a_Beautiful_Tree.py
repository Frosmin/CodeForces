






def res():
    n = int(input())
    permutacion = list(map(int, input().split()[:n]))

    intercambios = 0
    tamano_bloque = 2
    while tamano_bloque <= n:
        for i in range(0, n, tamano_bloque):
            mitad_tamano = tamano_bloque // 2
            inicio_izquierda = i
            inicio_derecha = i + mitad_tamano


            valor_izquierda = permutacion[inicio_izquierda]
            valor_derecha = permutacion[inicio_derecha]

 
            if abs(valor_izquierda - valor_derecha) != mitad_tamano:
                print(-1)
                return


            if valor_izquierda > valor_derecha:
                intercambios += 1

                for j in range(mitad_tamano):
                    permutacion[inicio_izquierda + j], permutacion[inicio_derecha + j] = \
                        permutacion[inicio_derecha + j], permutacion[inicio_izquierda + j]
        

        tamano_bloque *= 2

    print(intercambios)



k = int(input())
for _ in range(k):
    res()