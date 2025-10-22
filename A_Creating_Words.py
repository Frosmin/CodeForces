for _ in range(int(input())):
    word1, word2  = map(str,input().split())
    uno = word1[0]
    dos = word2[0]
    print( dos+word1[1:],uno+word2[1:])