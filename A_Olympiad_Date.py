s = int(input())
for _ in range(s):
    n = int(input())
    a = list(map(int, input().split()))
    cero = a.count(0)
    unos = a.count(1)
    dos = a.count(2)
    tres = a.count(3)
    cinco = a.count(5)
    if cero >= 3 and unos >= 1 and dos >= 2 and tres >= 1 and cinco >= 1:
        cero , unos, dos, tres, cinco = 0, 0, 0, 0, 0
        for i in range(n):
            if a[i] == 0 and cero < 3:
                cero +=1
            elif a[i] == 1 and unos < 1:
                unos += 1
            elif a[i] == 2 and dos < 2:
                dos += 1
            elif a[i] == 3 and tres < 1:
                tres += 1
            elif a[i] == 5 and cinco < 1:
                cinco += 1
            if cero == 3 and unos == 1 and dos == 2 and tres == 1 and cinco == 1:
                print(i+1)
                break
    else:
        print(0)
            
        
        
        
        
        
    #     if cero == 3:
    #         con = 0
    #         for i in range(n):
    #             if a[i] == 0:
    #                 con += 1
    #                 if con == 3:
    #                     print(i+1)
    #                     break
    # else:
    #     print(0)