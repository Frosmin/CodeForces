for _ in range(int(input())):
    pal = input()
    good = "abc"
    res = 0
    for i in range(3):
        if pal[i] == good[i]:
            res+= 1

    if res >= 1:
        print("YES")
    else:
        print("NO")
