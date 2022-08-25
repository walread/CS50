while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        amount = float(x) / float(y) * 100
        break
    except ValueError, ZeroDivisionError:
        pass

if amount >= 99:
    print("F")
elif amount <= 1:
    print("E")
else:
    print(amount) 