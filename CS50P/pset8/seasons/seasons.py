from datetime import date, timedelta
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time = (date.today() - birth)
    print(time.total_seconds()/60)

if __name__ == "__main__":
    main()
