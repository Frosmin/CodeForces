n = int(input())
responses = list(map(int,input().split()[:n]))
print("HARD" if responses[n-1] == 1 else "EASY")