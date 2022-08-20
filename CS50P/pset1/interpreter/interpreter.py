x, y, z = input("Expression: ").split(" ")

x = float(x)
z = float(z)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z

print(.2f{answer}))