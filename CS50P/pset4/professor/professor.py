import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
