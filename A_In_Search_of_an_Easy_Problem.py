n = int(input())
responses = list(map(int,input().split()[:n]))
print("HARD" if responses.count(1) != 0 else "EASY")