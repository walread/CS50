from datetime import date
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    print(birth, today)

if __name__ == "__main__":
    main()
