# Ejemplo: buscar si alguno de los caracteres está en la palabra
chars = set("ABC")
word = "SAMUEL"

# 1) Saber si hay alguna coincidencia
hay = bool(chars & set(word))
print(hay)  # True

# 2) Encontrar la primera posición (índice 0-based), -1 si no existe
first_index = next((i for i, ch in enumerate(word) if ch in chars), -1)
print(first_index)  # 1

# 3) Todas las posiciones donde aparece alguno de los caracteres
positions = [i for i, ch in enumerate(word) if ch in chars]
print(positions)  # [1]

# Si prefieres posiciones 1-based:
positions_1_based = [i+1 for i in positions]
print(positions_1_based)  # [2]





a = set("HQ9S")       # {'H','Q','9'}
b = set("SAMUEL")    # {'S','A','M','U','E','L'}

print(bool(a & b))         # intersección: conjunto de caracteres comunes -> set() o {'A'} si A está en ambos
print("H" in a)      # True

print(a in b)


# ejemplo: tus sets
a = set("HQ9S")
b = set("SAMUEL")

# 1) ¿hay algún carácter común? (lo que quieres normalmente)
print(bool(a & b))      # True si intersección no vacía

# 2) ¿todos los caracteres de a están en b? (subconjunto)
print(a <= b)           # True si a es subconjunto de b

# 3) si realmente necesitas usar membership con un conjunto como elemento,
#    convierte a en frozenset (hashable) y haz que b contenga ese frozenset
af = frozenset(a)
B = {af}
print(af in B)          # True




# para unir una lista
lista = [1,2,3]
print(" ".join(map(str, lista)))



print(" ".join(input().split("WUB")).strip())