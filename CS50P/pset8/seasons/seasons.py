from datetime import date
import inflect
p = inflect.engine()
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    time = int((today - birth).total_seconds()/60)
    word_time = p.number_to_words(time).replace(" and", "")
    print(f"{word_time} minutes")

if __name__ == "__main__":
    main()
