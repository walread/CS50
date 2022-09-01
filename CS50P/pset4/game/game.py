import random
import sys

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
        if guess < 1:
            pass
        elif guess > level:
            print("Too large!")
        elif guess < level:
            print("Too small!")
        else:
            sys.exit("Just right!")
    except ValueError:
        pass
