import random


def main():
    n = get_level()
    x = generate_integer(n)
    y = generate_integer(n)
    answer = int(input(f"{x} + {y} = "))
    if answer == (x + y):
        print("Correct")
    else:
        print("EEE")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
