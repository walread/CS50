import csv, sys
from tabulate import tabulate

pizzas = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
name, type = sys.argv[1].split(".")
if type != "csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
    for row in reader:
        pizzas.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizzas, tablefmt="grid"))
