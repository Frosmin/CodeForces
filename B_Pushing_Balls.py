import sys
#hola
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(n):
            line = sys.stdin.readline().strip()
            grid.append(list(line))
        valid = True
        for i in range(n):
            if not valid:
                break
            for j in range(m):
                if grid[i][j] == '1':
                    row_ok = True
                    for k in range(j + 1):
                        if grid[i][k] != '1':
                            row_ok = False
                            break
                    col_ok = True
                    for k in range(i + 1):
                        if grid[k][j] != '1':
                            col_ok = False
                            break
                    if not row_ok and not col_ok:
                        valid = False
                        break
            if not valid:
                break
        print("YES" if valid else "NO")

if __name__ == "__main__":
    main()