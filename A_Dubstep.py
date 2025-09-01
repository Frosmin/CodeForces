# WUB 

cancion = input()
lst = []
i = 0
while i < len(cancion):
    if len(cancion)-i >= 3: 
        if cancion[i] == "W" and cancion[i+1] == "U" and cancion[i+2] == "B":
            if lst and lst[-1]  == " ":
                i += 3
                pass
            else:
                lst.append(" ")
                i += 3
        else:
            lst.append(cancion[i])
            i+=1
    else:
        lst.append(cancion[i])
        i+=1

    
print("".join(map(str,lst)))