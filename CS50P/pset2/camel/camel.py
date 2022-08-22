name = input("camelCase: ")

for c in range(len(name)):
    if name[c] == 'A':
        name = name[:c] + "_" + name[c:]
        c += 1

print("snake_case:", name.lower())