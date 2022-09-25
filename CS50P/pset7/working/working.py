import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if matches == None:
        raise ValueError
    else:
        if None in matches.groups():
            return "Includes none"
        else:
            return "Doesn't include none"


if __name__ == "__main__":
    main()
