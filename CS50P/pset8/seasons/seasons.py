from datetime import date
import sys


def main():
    try:
        birth = date(input("Date of Birth: ").split("-"))
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
