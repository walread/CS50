import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
        return matches.groups()
    except AttributeError:
        return "ValueError"


if __name__ == "__main__":
    main()
