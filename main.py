import argparse
from ALU import total


def main():
    parser = argparse.ArgumentParser(description='add or multiply two numbers')
    parser.add_argument('arg1', type=int,
                        help='first argment')
    parser.add_argument('arg2', type=int,
                        help='second argment')
    args = parser.parse_args()
    a = args.arg1
    b = args.arg2

    print(a, b)

    print(total(1, 2))


if __name__ == '__main__':
    main()
