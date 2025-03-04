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

def jugar(jugador1, jugador2):
    mesa = []
    ultimo_jugador_figura = None
    
    
    turno_jugador2 = True
    
    while len(jugador1) > 0 and len(jugador2) > 0:
        
        if turno_jugador2:
            jugador = jugador2
            nombre_jugador = "jugador2"
        else:
            jugador = jugador1
            nombre_jugador = "jugador1"
        
        
        if len(jugador) == 0:
            break
            
        
        carta = jugador.pop(0)
        mesa.append(carta)
        
        
        valor = tipo(carta)
        
        if valor > 0:  
            
            ultimo_jugador_figura = nombre_jugador
            
           
            turno_jugador2 = not turno_jugador2
            
           
            cartas_a_cubrir = valor
            figura_cubierta = False
            
            
            if turno_jugador2:
                jugador_cubre = jugador2
            else:
                jugador_cubre = jugador1
                
            for _ in range(cartas_a_cubrir):
                if len(jugador_cubre) == 0:
                    break  
                    
                carta_respuesta = jugador_cubre.pop(0)
                mesa.append(carta_respuesta)
                
                
                if tipo(carta_respuesta) > 0:
                    figura_cubierta = True
                    if turno_jugador2:
                        ultimo_jugador_figura = "jugador2"
                    else:
                        ultimo_jugador_figura = "jugador1"
                    break
            
            
            if not figura_cubierta:
                if ultimo_jugador_figura == "jugador1":
                    jugador1.extend(mesa)
                else:
                    jugador2.extend(mesa)
                mesa = []
                
                
                turno_jugador2 = (ultimo_jugador_figura == "jugador2")
        else:
          
            turno_jugador2 = not turno_jugador2
    
    # Determinar el ganador
    if len(jugador1) == 0:
        return "2" + str(len(jugador2)).rjust(3)
    else:
        return "1" + str(len(jugador1)).rjust(3)

if __name__ == '__main__':
    while True:
        linea = input()
        if linea == '#':
            break
            
        mazo = []
        mazo.extend(linea.split())
        
       
        for _ in range(3):
            linea_adicional = input()
            mazo.extend(linea_adicional.split())
        
        
        jugador1 = []  
        jugador2 = []  
        
        for i in range(52):
            if i % 2 == 0:
                jugador2.append(mazo[i])
            else:
                jugador1.append(mazo[i])
        
        resultado = jugar(jugador1, jugador2)
        print(resultado)
