a,b = map(int, input().strip().split())
if not(1<=a<=b<=10):
    raise ValueError("Error")
n = 0
while a <= b:
    a *= 3
    b *= 2
    n += 1
print(n)