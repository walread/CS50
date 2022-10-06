from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birth = input("Date of Birth: ")
    print(convert(birth))


def convert(birth):
    try:
        birth = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    time = int((today - birth).total_seconds()/60)
    word_time = p.number_to_words(time).replace(" and", "").capitalize()
    return f"{word_time} minutes"


if __name__ == "__main__":
    main()
