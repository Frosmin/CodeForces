
timu = "Timur"
for _ in range(int(input())):
    n = int(input())
    palabra = input()

    if n == 5 and sorted(palabra) == sorted(timu):
        print("YES")
    else:
        print("NO")

