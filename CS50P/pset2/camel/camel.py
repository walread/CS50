camel = input("camelCase: ")

snake = camel[0].lower()
for c in camel:
    if c.isupper():
        snake += "_"
    snake += c.lower()

print("snake_case:", snake) 