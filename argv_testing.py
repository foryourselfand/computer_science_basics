import argparse


def main():
    parser = argparse.ArgumentParser(description = 'test description')

    parser.add_argument('integer')

    parser.add_argument('--file', '-f')

    parser.parse_args()


if __name__ == '__main__':
    main()
