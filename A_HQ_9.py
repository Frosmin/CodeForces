word = input()

buscar = set("HQ9")

print("YES" if bool(buscar & set(word)) else "NO")