
def an(x, y, id, w, h, v):
    """
    Comprueba si un punto (x, y) está en el borde del rectángulo (0,0) a (w,h).
    Si es así, lo añade a la lista correspondiente al borde y devuelve 1.
    """
    if y == 0:
        v[0].append((x, id))
        return 1
    elif x == w:
        v[1].append((y, id))
        return 1
    elif y == h:
        v[2].append((-x, id))
        return 1
    elif x == 0:
        v[3].append((-y, id))
        return 1
    return 0



w, h = map(int, input().split())
n = int(input())
# v es una lista de 4 listas, una para cada borde del rectángulo:
# 0: abajo, 1: derecha, 2: arriba, 3: izquierda
v = [[] for _ in range(4)]

# freq[i] cuenta cuántos de los dos puntos del par i están en el borde
freq = [0] * n

for i in range(n):
    
    a, b, c, d = map(int, input().split())
    # Comprueba si los dos puntos están en el borde y actualiza la frecuencia
    freq[i] += an(a, b, i, w, h, v)
    freq[i] += an(c, d, i, w, h, v)
    
# 'a' será una lista única con todos los puntos del borde ordenados
a = []
for i in range(4):
    # Ordena los puntos en cada borde
    v[i].sort()
    # Añade los puntos ordenados a la lista 'a'
    a.extend(v[i])
    
st = []  # Pila para verificar el anidamiento correcto
cnt = [0] * n # Contador para saber si es el primer o segundo punto de un par

for _, x_id in a:
    # Solo procesamos pares donde ambos puntos estaban en el borde
    if freq[x_id] != 2:
        continue
        
    cnt[x_id] += 1
    if cnt[x_id] == 2: # Si es el segundo punto del par
        # La pila no debe estar vacía y el elemento superior debe ser el mismo ID
        if not st or st[-1] != x_id:
            print("N")
            exit()
        st.pop() # Si coincide, lo sacamos de la pila
    else: # Si es el primer punto del par
        st.append(x_id) # Lo metemos en la pila
        

if not st:
    print("Y")
else:
    print("N")

# ### Explicación del Código

# El problema que este código resuelve es determinar si un conjunto de `n` cuerdas, cada una conectando dos puntos en el perímetro de un rectángulo, se pueden dibujar sin que se crucen entre sí.

# 1.  **Lectura de Entrada**:
#     *   Se leen las dimensiones del rectángulo `w` (ancho) y `h` (alto).
#     *   Se lee el número de cuerdas `n`.
#     *   Para cada una de las `n` cuerdas, se leen las coordenadas de sus dos puntos extremos.

# 2.  **Almacenamiento de Puntos del Borde**:
#     *   La función `an` verifica si un punto dado está en uno de los cuatro bordes del rectángulo.
#     *   Se utiliza una lista de listas `v` (de tamaño 4) para almacenar los puntos de cada borde por separado (0: abajo, 1: derecha, 2: arriba, 3: izquierda).
#     *   A cada punto se le asocia un `id` (de 0 a `n-1`) que identifica a qué cuerda pertenece.
#     *   La lista `freq` se usa para contar, para cada cuerda, cuántos de sus dos puntos extremos están realmente en el borde. Solo nos interesan las cuerdas donde ambos puntos están en el borde (`freq[i] == 2`).

# 3.  **Ordenamiento de Puntos**:
#     *   Los puntos en cada borde se ordenan. La clave de ordenación (`x`, `y`, `-x`, `-y`) está elegida de tal manera que al concatenar las listas de los 4 bordes en orden (abajo, derecha, arriba, izquierda), obtenemos una única lista `a` con todos los puntos ordenados a lo largo del perímetro en el sentido de las agujas del reloj.

# 4.  **Verificación con una Pila**:
#     *   El problema de verificar si las cuerdas se cruzan se reduce a un problema de paréntesis bien balanceados. Imagina que recorres el perímetro: cuando encuentras el primer punto de una cuerda, es como abrir un paréntesis `(`. Cuando encuentras el segundo punto, es como cerrar un paréntesis `)`.
#     *   Para que no haya cruces, las cuerdas deben estar anidadas correctamente. Por ejemplo, `( ( ) )` está bien, pero `( [ ) ]` (un cruce) no lo está.
#     *   Se recorre la lista ordenada `a` de puntos del perímetro.
#     *   Se usa una pila `st`:
#         *   Cuando se encuentra el **primer** punto de una cuerda (con `id`), se mete su `id` en la pila.
#         *   Cuando se encuentra el **segundo** punto de una cuerda, se comprueba si el `id` en la cima de la pila es el mismo.
#             *   Si lo es, significa que la cuerda se "cierra" correctamente, y se saca el `id` de la pila.
#             *   Si no lo es, o si la pila está vacía, significa que hay un cruce de cuerdas. El programa imprime "N" y termina.

# 5.  **Resultado Final**:
#     *   Si se procesan todos los puntos y la pila queda vacía, significa que todas las cuerdas se abrieron y cerraron en el orden correcto, sin cruces. El programa imprime "Y".
#     *   Si al final la pila no está vacía, significa que algunas cuerdas nunca se "cerraron", lo cual también es una condición inválida, por lo que se imprimiría "N".