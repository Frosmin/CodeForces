for _ in range(int(input())):
    pal = input()
    res = ""
    for item in pal:
        if item == 'q':
            res+= 'p'
        elif item == 'p':
            res+= 'q'
        else:
            res+= 'w'
    print(res[::-1])