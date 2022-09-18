import csv, sys

if len(sys.argv) > 3:
    print("Too many command-line arguments")
elif len(sys.argv) < 3:
    print("Too few command-line arguments")

try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        with open(sys.argv[2], "a") as after:
            writer = csv.DictWriter(after)
            for row in before:
except FileNotFoundError:
    sys.exit(f"Cound not read {sys.argv[1]}")
    