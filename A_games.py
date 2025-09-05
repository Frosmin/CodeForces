n = int(input())
dic = {}
for i in range(n):
    a,b = map(int,input().split())
    for item in dic:
        # if item == a:
        #    item+=1
        # elif item == b:
        #      item+=1
        # else:
        #      dic[item] = 0
print(dic)