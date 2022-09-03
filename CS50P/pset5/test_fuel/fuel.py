def main():
    while True:
    try:
        fraction = input("Fraction: ")
        if convert(fraction) <= 100:
            break
    except (ValueError, ZeroDivisionError):
        pass
if amount >= 99:
    print("F")
elif amount <= 1:
    print("E")
else:
    print(f"{amount}%")


def convert(fraction):
    x, y = fraction.split("/")
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
