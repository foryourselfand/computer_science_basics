from sys import argv


def main():
    args = argv[1:][0]
    args_split = args.split(' ')[:2]
    first, second = map(int, args_split)
    
    print(-2 ** 15 <= first + second <= 2 ** 15 - 1)


if __name__ == '__main__':
    main()
