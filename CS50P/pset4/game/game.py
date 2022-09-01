import random

while True:
    n = input("Level: ")
    if n.isdigit():
        break

level = random.randint(1, int(n))

while True:
    guess = input("Guess: ") 