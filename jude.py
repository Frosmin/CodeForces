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

def buscar_figura(mazo, n):
    for i in range(n):
        if mazo[i] != 0:
            return mazo[i], mazo





def jugar(jugador1, jugador2):
    mesa = []
    turno = 2
    figura = 0
    while len(jugador1) > 0 and len(jugador2) > 0:
        if turno == 2:
            if figura != 0:
                for i in range(figura):
                    if jugador2[i] != 0:
                        figura = jugador2[i]
                        mesa.append(jugador2.pop(0))
                        i -= 1
                        figura -= 1
                        turno = 1
                        break
                    else:
                        mesa.append(jugador2.pop(0))
                    turno = 1
            else:
                carta_jugador2 = jugador2[0]
                if carta_jugador2 == 0:
                    mesa.append(jugador2.pop(0)) #mueve la carta a la mesa
                    turno = 1
                else:
                    figura = jugador2[0]
                    mesa.append(jugador2.pop(0))
                    turno = 1
        else:
            if figura != 0:
                if figura <= len(jugador1):
                    for i in range(figura):
                        if jugador1[i] != 0:
                            figura = jugador1[i]
                            mesa.append(jugador1.pop(0))
                            i -= 1
                            figura -= 1
                            turno = 2
                            break
                        else:
                            mesa.append(jugador1.pop(0))
                        turno = 2
                else:
                    print('Jugador 2 gana')
                    break
            else:   
                carta_jugador1 = jugador1[0]
                if carta_jugador1 == 0:
                    mesa.append(jugador1.pop(0)) #mueve la carta a la mesa
                    turno = 2
                else:
                    figura = jugador1[0]
                    turno = 2
    print("mesa--------------------")
    print(mesa) 
    print("jugadores----------------")           
    print(jugador1)
    print(jugador2)
                
                
                    
            
            
            




if __name__ == '__main__':
    mazo = list(map(str, input().split()))
    mazo_numeros = convertir_mazo(mazo)
    
   
   
    jugador1 = []
    jugador2 = []    
        
    for i in range(52):
        if i % 2 == 0:
                jugador2.append(mazo_numeros[i])
        else:
                jugador1.append(mazo_numeros[i])
    # print(mazo)
    # print(mazo_numeros)
    # print(jugador1)
    # print(jugador2)
    jugar(jugador1, jugador2)
    
# HA H3 H4 CA SK S5 C5 S6 C4 D5 H7 HJ HQ D4 D7 SJ DT H6 S9 CT HK C8 C9 D6 CJ C6 S8 D8 C2 S2 S3 C7 H5 DJ S4 DQ DK D9 D3 H9 DA SA CK CQ C3 HT SQ H8 S7 ST H2 D2