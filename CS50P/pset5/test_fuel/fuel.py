def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()


while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        amount = round(int(x) / int(y) * 100)
        if amount <= 100:
            break
    except (ValueError, ZeroDivisionError):
        pass

if amount >= 99:
    print("F")
elif amount <= 1:
    print("E")
else:
    print(f"{amount}%")
