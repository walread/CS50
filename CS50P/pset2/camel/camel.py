name = input("camelCase: ")

for c in name:
    if c.isupper():
        print(c)

print("snake_case:", name.lower())