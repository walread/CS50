import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

level = random.randint(1, int(n))
print(level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass