import csv, sys

if len(sys.argv) > 3:
    print("Too many command-line arguments")
elif len(sys.argv) < 3:
    print("Too few command-line arguments")

list = []

try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        for row in before:
            , last, house = row.split(",")
            list.append({"first": first.lstrip(), "last": last, "house": house})
except FileNotFoundError:
    sys.exit(f"Cound not read {sys.argv[1]}")

print(list)
