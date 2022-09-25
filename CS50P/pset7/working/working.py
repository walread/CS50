import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    try:
        if None in matches.group(2):
            return "None found"
        else:
            return matches.group(2)
    except AttributeError:
        raise ValueError


if __name__ == "__main__":
    main()
