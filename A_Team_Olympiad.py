# res = [0]*3
# n = int(input())
# lst = list(map(int,input().split()[:n]))
# for item in lst:
#     res[item-1] +=1


# minimo = min(res)
# print(0 if minimo == 0 else minimo)



res = [[],[],[]]
n = int(input())
lst = list(map(int,input().split()[:n]))

for i in range(n):
    elemto  = lst[i]
    res[elemto-1].append(i+1)


minimo = min(len(res[0]),len(res[1]),len(res[2]))
if minimo==0:
    print(0)
    exit()
else:
    print(minimo)
    for i in range(minimo):
        print(res[0][i], res[1][i], res[2][i])

    



