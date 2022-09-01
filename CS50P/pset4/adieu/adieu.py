import inflect

names = []

while True:
    try:
        name = input("Name: ")
        names += name
    except EOFError:
        break
        print()

names = p.join(names)