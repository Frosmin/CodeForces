dic  = {
    "T":4,
    "C":6,
    "O":8,
    "D":12,
    "I":20
}
res= 0
n = int(input())
for _ in range(n):
    res += dic.get(input()[0],0)
print(res)