import csv, sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

list = []

try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        for row in reader:
            list.append(row)
except FileNotFoundError:
    sys.exit(f"Cound not read {sys.argv[1]}")

del list[0]
new_list = []

for row in list:
    last, first, house = row.split(",")

print(list)
