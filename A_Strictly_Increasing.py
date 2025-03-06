n = int(input())
a = list(map(int,(input().split())))
def ejer(a,n):
    for i in range(n-1):
        if a[i] >= a[i+1]:
            return "No"
    return "Yes"   

print(ejer(a,n))


