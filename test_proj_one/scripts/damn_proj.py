from math import sqrt
from colorama import Fore
from colorama import Back


def main():
    result = int(sqrt(121) + 78)
    print(Fore.GREEN + Back.WHITE + str(result))


if __name__ == '__main__':
    main()
