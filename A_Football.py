n = input()
cero = 0
uno = 0
for i in range(len(n)):
    if n[i] == '0':
        cero += 1
        uno = 0
    elif n[i] == '1':
        uno += 1
        cero = 0
    if cero >= 7 or uno >= 7:
        print("YES")
        exit()
print("NO")

        
