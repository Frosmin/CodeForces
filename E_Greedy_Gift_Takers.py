def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    
    for i in range(n):
        if c_list[i] == n - 1:
            result = n - i - 1
            print(str(result))
            exit()

                

    print('0')

if __name__ == '__main__':
    main()