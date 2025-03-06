def tipo(carta):
    rank = carta[1]
    if rank == 'J':
        return 1
    elif rank == 'Q':
        return 2
    elif rank == 'K':
        return 3
    elif rank == 'A':
        return 4
    else:
        return 0
    
def convertir_mazo(mazo):
    nuevo_mazo = []
    for carta in mazo:
        nuevo_mazo.append(tipo(carta))
    return nuevo_mazo

def jugar(jugador1, jugador2):
    # jugador1 es el dealer (player 1)
    # jugador2 es el non-dealer (player 2)
    mesa = []
    turno = 2  # Comienza el non-dealer (jugador 2)
    figura = 0
    ultimo_jugador_figura = None
    
    while True:
        # Verificar si algún jugador ya no tiene cartas
        if len(jugador1) == 0:
            return 2, len(jugador2)
        if len(jugador2) == 0:
            return 1, len(jugador1)
            
        # Turno del jugador 2 (non-dealer)
        if turno == 2:
            if figura != 0:
                # Tiene que cubrir una figura
                cartas_a_jugar = figura
                
                # Verificar si tiene suficientes cartas
                if cartas_a_jugar > len(jugador2):
                    return 1, len(jugador1)
                
                figura_encontrada = False
                
                # Jugar el número requerido de cartas o hasta encontrar una figura
                for _ in range(cartas_a_jugar):
                    if len(jugador2) == 0:
                        return 1, len(jugador1)
                        
                    carta = jugador2.pop(0)
                    mesa.append(carta)
                    
                    if carta != 0:  # Si es una carta de figura
                        figura = carta
                        ultimo_jugador_figura = 2
                        figura_encontrada = True
                        break
                
                if not figura_encontrada:
                    # Si completó la secuencia sin encontrar figura
                    # El último jugador que jugó figura toma las cartas
                    if ultimo_jugador_figura == 1:
                        jugador1.extend(mesa)
                    else:
                        jugador2.extend(mesa)
                    mesa = []
                    figura = 0
                    ultimo_jugador_figura = None
                
                turno = 1
            else:
                # Jugar carta normal
                if len(jugador2) == 0:
                    return 1, len(jugador1)
                    
                carta = jugador2.pop(0)
                mesa.append(carta)
                
                if carta != 0:  # Si es una carta de figura
                    figura = carta
                    ultimo_jugador_figura = 2
                
                turno = 1
        
        # Turno del jugador 1 (dealer)
        else:
            if figura != 0:
                # Tiene que cubrir una figura
                cartas_a_jugar = figura
                
                # Verificar si tiene suficientes cartas
                if cartas_a_jugar > len(jugador1):
                    return 2, len(jugador2)
                    
                figura_encontrada = False
                
                # Jugar el número requerido de cartas o hasta encontrar una figura
                for _ in range(cartas_a_jugar):
                    if len(jugador1) == 0:
                        return 2, len(jugador2)
                        
                    carta = jugador1.pop(0)
                    mesa.append(carta)
                    
                    if carta != 0:  # Si es una carta de figura
                        figura = carta
                        ultimo_jugador_figura = 1
                        figura_encontrada = True
                        break
                
                if not figura_encontrada:
                    # Si completó la secuencia sin encontrar figura
                    # El último jugador que jugó figura toma las cartas
                    if ultimo_jugador_figura == 1:
                        jugador1.extend(mesa)
                    else:
                        jugador2.extend(mesa)
                    mesa = []
                    figura = 0
                    ultimo_jugador_figura = None
                
                turno = 2
            else:
                # Jugar carta normal
                if len(jugador1) == 0:
                    return 2, len(jugador2)
                    
                carta = jugador1.pop(0)
                mesa.append(carta)
                
                if carta != 0:  # Si es una carta de figura
                    figura = carta
                    ultimo_jugador_figura = 1
                
                turno = 2

if __name__ == '__main__':
    while True:
        entrada = input().strip()
        if entrada == '#':
            break
            
        mazo = entrada.split()
        
        # Leer el resto de las líneas (4 líneas en total con 13 cartas cada una)
        for _ in range(3):
            linea = input().strip()
            mazo.extend(linea.split())
            
        mazo_numeros = convertir_mazo(mazo)
        
        # El dealer (jugador 1) recibe la última carta
        # El non-dealer (jugador 2) recibe la primera carta
        jugador1 = []  # dealer
        jugador2 = []  # non-dealer
        
        # Corregir la distribución de cartas según las reglas:
        # "...la primera carta va al non-dealer, la segunda al dealer, y así sucesivamente..."
        for i in range(52):
            if i % 2 == 0:
                jugador2.append(mazo_numeros[i])  # Non-dealer recibe cartas pares (comenzando por 0)
            else:
                jugador1.append(mazo_numeros[i])  # Dealer recibe cartas impares
                
        ganador, cartas = jugar(jugador1, jugador2)
        print(f"{ganador}{cartas:3d}")