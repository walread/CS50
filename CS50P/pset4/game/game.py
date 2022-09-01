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
        guess > 0
    except ValueError:
        pass
    if guess > level:
        print("Too large!")
    elif guess < level:
        print("Too small!")
    else:
        print("Just right!") 