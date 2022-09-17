import sys

lines = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
name, type = sys.argv[1].split(".")
if type != "py"
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        for line in file:
            lines.append(line.lstrip())
except FileNotFoundError:
    sys.exit("File does not exist")

counter = 0
for line in lines:
    if not line.startswith("#") and len(line) > 0:
        counter += 1

print(counter)