n = int(input())
for i in range(n):

    s = int(input())
    if s != 1:
        raiz = s ** 0.5
        if raiz % 1 == 0:
            num = raiz / 2
            if num % 1 != 0:
                print(f"{int(num)} {int(num) + 1}")
            else:
                print(f"{int(num)} {int(num)}")
        else:
            print(-1)
    else:
        print(f"{0} {1}")