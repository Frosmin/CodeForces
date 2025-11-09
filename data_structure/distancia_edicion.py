def distancia_edicion(cadena1, cadena2):
    len_cadena1 = len(cadena1)+1
    len_cadena2 = len(cadena2)+1
    
    matrix = [[0 for n in range(len_cadena2)] for m in range(len_cadena1)]


    for i in range(len_cadena1):
        matrix[i][0] = i
    for j in range(len_cadena2):
        matrix[0][j] = j

    for i in range(1, len_cadena1):
        for j in range(1, len_cadena2):
            cost = 0 if cadena1[i-1] == cadena2[j-1] else 1
            matrix[i][j] = min(matrix[i-1][j] +1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)
    return matrix[len_cadena1-1][len_cadena2-1]


print(distancia_edicion("amor", "amar"))
