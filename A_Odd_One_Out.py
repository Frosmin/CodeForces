n = int(input())
dic = {}

for _ in range(n):
    lst = list(map(int,input().split()[:n]))
    for item in lst:
        if item in dic:
            dic[item] +=1
        else:
            dic[item] = 1
    print(min(dic, key=dic.get))
    dic = {}