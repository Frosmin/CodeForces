n = int(input())
lst = list(map(int,input().split()[:n]))

a = sum(lst)
uno  = lst.count(1)
dos  = lst.count(2)
tres  = lst.count(3)
cuatro = lst.count(4)
res  = cuatro
niños_solos = 0

if uno > tres:
    res += tres
    niños_solos += uno-tres
elif uno == tres:
    res+= tres
else:
    res += uno
    res +=  (tres-uno)

res += dos//2
niños_solos += (dos%2)*2

res += niños_solos//4
if niños_solos%4 != 0:
    res+=1


     
print(res)