n = int(input())
lst = []
i = 1
for _ in range(n):
    num = int(input())
    if len(lst) < num:
        while len(lst) != num:
            if i % 3 != 0 and i%10 != 3:
                    lst.append(i)
                    i+=1
            else:
                i+=1
    else:
        print(lst[num])                  
    print(lst[num-1])
            