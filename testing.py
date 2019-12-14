from collections import namedtuple

def main():
    Test = namedtuple('Test', ['data', 'is_command'])
    test = Test('000', True)
    print(type(test))
    print(test)
    print(test.data)


if __name__ == '__main__':
    main()
