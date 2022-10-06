from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    time = int((today - birth).total_seconds()/60)
    word_time = p.number_to_words(time).replace(" and", "").capitalize()
    print(f"{word_time} minutes")

if __name__ == "__main__":
    main()
