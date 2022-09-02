import random


def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        for j in range(4):
            if j < 3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                    if answer != (x + y):
                        raise ValueError
                    else:
                        score += 1
                        break
                except ValueError:
                    print("EEE")
            else:
                print(f"{x} + {y} = {x + y}")
    print(f"{score}/10")


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
