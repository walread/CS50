import random

while True:
    n = input("Level: ")
    if n.isdigit():
        break

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