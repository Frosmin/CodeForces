n = int(input())
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

res = lambda x,y: sqt((x1-x)**2 + (y1-y)**2) + sqt((x2-x)**2 + (y2-y)**2) + sqt((x1-x2)**2 + (y1-y2)**2)