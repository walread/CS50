from datetime import date
import inflect
p = inflect.engine()
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    today = date.fromisoformat("2000-01-01")
    time = int(today - birth).total_seconds()/60
    words = p.number_to_words(time).replace(" and", "")
    print(f"{words} minutes")

if __name__ == "__main__":
    main()
