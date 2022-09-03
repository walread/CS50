def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            if percentage <= 100:
                print(gauge(percentage))
                break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
