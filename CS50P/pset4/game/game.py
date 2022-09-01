import random

while True:
    n = input("Level: ")
    try:
        int(n) > 0
        break
    except ValueError:
        pass

level = random.randint(1, int(n))
print(level)

while True:
    guess = input("Guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess > level:
            print("Too large!")
        elif guess < level:
            print("Too small")
        else:
            print("Just right!")
            break