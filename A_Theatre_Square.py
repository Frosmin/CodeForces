n,m,a = map(int, input().split())


def redondeo(n):
    if int(n) == n:
        return int(n)
    else:
        return int(n) + 1

divi = n / a
divi = redondeo(divi)
divi2 = m / a
divi2 = redondeo(divi2)
print(divi*divi2)