from datetime import date
import inflect
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time = (date.today() - birth).seconds()
    print(time)

if __name__ == "__main__":
    main()
