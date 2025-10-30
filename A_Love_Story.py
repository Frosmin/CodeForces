code = "codeforces"

for _ in range(int(input())):
    pal = input()
    res = 0
    for i in range(10):
        if pal[i] != code[i]:
            res+=1

    print(res)