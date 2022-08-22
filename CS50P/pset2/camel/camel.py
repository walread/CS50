name = input("camelCase: ")

for c in range(len(name)):
    if c == 'A':
        name = name[:c]

print("snake_case:", name.lower())