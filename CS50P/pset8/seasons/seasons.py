from datetime import date
import inflect
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time = int((date.today() - birth).total_seconds()/60)
    print(time)

if __name__ == "__main__":
    main()
