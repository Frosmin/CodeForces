for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()[:n]))
    for i in range (n-1):
        valor=(abs(lst[i]-lst[i+1]))
        if valor != 7 and valor != 5 :
            print("NO")
            break
    else:
        print("YES")