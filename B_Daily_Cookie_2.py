def main():
    n,d = map(int,input().split())
    s = list(map(str ,input()))
    i = 0
    while d > 0:
        if s[(n-1)-i] == "@":
            d -= 1
            s[(n-1)-i] = "."
        i += 1
    print(''.join(s))



if __name__ == "__main__":
    main()