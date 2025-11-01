for _ in range(int(input())):
    word = input()
    mid = len(word)//2
    if word[:mid] == word[mid:]:
        print("YES")
    else:
        print("NO")

