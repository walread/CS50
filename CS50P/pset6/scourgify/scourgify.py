import csv, sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

list = []

try:
    with open(sys.argv[1]) as before:
        reader = csv.reader(before)
        for row in before:
            last, first, house = row.replace('"', "").split(",")
            list.append({"first": first.lstrip(), "last": last, "house": house.replace("/n", "")})
except FileNotFoundError:
    sys.exit(f"Cound not read {sys.argv[1]}")

print(list)
