import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if matches.group(1) == "13":
        raise ValueError
    else:
        return matches.groups()


...


if __name__ == "__main__":
    main()
