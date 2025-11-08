patron  = "ABC"
cadena  = "ABCASDGAABC"

def conseguir_hash(patron):
    res = 0
    for item in patron:
        res += ord(item)
    return res



hash_patron = conseguir_hash(patron)
lista_res = []
for i in range(len(cadena)-2):
    cadena_a_probar = cadena[i:i+3]
    if conseguir_hash(cadena_a_probar) ==  hash_patron:
        for j in range(len(patron)):
            if patron[j] != cadena_a_probar[j]: 
                break
        else:
            lista_res.append(i)
    

print(lista_res)



patron = "ABC"
cadena = "ABCASDGAABC"

def rabin_karp(patron, cadena):
    n, m = len(cadena), len(patron)
    base = 256
    mod = 10**9 + 7

    # Precalcula base^(m-1) % mod
    h = pow(base, m-1, mod)

    # Calcula hash del patrón y de la primera ventana
    hash_patron = 0
    hash_cadena = 0
    for i in range(m):
        hash_patron = (hash_patron * base + ord(patron[i])) % mod
        hash_cadena = (hash_cadena * base + ord(cadena[i])) % mod

    res = []
    for i in range(n - m + 1):
        if hash_cadena == hash_patron:
            if cadena[i:i+m] == patron:
                res.append(i)
        if i < n - m:
            # Actualiza hash de la ventana
            hash_cadena = (hash_cadena - ord(cadena[i]) * h) % mod
            hash_cadena = (hash_cadena * base + ord(cadena[i + m])) % mod
            hash_cadena = (hash_cadena + mod) % mod  # Evita negativos
    return res

print(rabin_karp(patron, cadena))