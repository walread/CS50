from datetime import date
import sys


def main():
    try:
        birth = input("Date of Birth: ")
        print(birth)
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
