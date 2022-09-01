import inflect

names = []

while True:
    try:
        name = input("Name: ")
        names += name
    except EOFError:
        break

names = inflect.join(names)

print("Adieu, adieu, to", names)
