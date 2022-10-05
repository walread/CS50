from datetime import date
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time = (date.today() - birth)
    print(date(time).strftime())

if __name__ == "__main__":
    main()
