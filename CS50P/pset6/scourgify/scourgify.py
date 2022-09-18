import csv, sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

list = []

try:
    with open(sys.argv[1]) as before:
        reader = csv.reader(before)
        for row in reader:
            list.append(row)
except FileNotFoundError:
    sys.exit(f"Cound not read {sys.argv[1]}")

del list[0]

with open(sys.argv[2], "a") as after:
    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
    for item in list:
        last, first = item[0].split(",")
        writer.writerow({"first": first.lstrip(), "last": last, "house": item[1]})
