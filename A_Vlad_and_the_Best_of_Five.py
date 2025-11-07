for _ in range(int(input())):
    print("A" if (a:=input()).count("A")> a.count("B") else "B")