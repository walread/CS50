import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    try:
        if None in matches.groups(1,3,4,5):
            return "None found"
        else:
            return "None not found"
    except AttributeError:
        raise ValueError


if __name__ == "__main__":
    main()
