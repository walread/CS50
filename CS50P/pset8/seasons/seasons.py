from datetime import date, timedelta
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time = total_seconds(date.today() - birth)
    print(time)

if __name__ == "__main__":
    main()
