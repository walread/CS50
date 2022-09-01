import random

while True:
    n = input("Level: ")
    try:
        n = int(n)
        if n > 0:
            level = random.randint(1, int(n))
            print(level)
            break
    except ValueError:
        pass

