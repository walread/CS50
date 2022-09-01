import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            level = random.randint(1, int(n))
            print(level)

    except ValueError:
        pass

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