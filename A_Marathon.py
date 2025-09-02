n = int(input())
for _ in range(n):
    res = 0
    run = list(map(int,input().split()))
    tim = run.pop(0)
    for item in run:
        if item > tim:
            res+=1
    print(res)