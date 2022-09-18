import csv, sys

if len(sys.argv) > 3:
    print("Too many command-line arguments")
elif len(sys.argv) < 3:
    print("Too few command-line arguments")

try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        for row in reader: