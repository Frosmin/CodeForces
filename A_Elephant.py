#1 2 3 4 5
# print(1000000%5)
# print(5)
dis = int(input())
falta = dis %5
res = 0
if dis < 5:
    print(1)
elif falta != 0 and dis > 5:
    res += dis//5
    res += 1
    print(res)
else: 
    print(dis//5)
