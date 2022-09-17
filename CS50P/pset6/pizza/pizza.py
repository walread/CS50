import csv, sys

pizzas = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        pizzas.append(row)

print(tabulate(pizzas))