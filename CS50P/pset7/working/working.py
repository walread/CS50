import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if matches == None:
        raise ValueError
    else:
        if matches.group(3) == "PM":
            matches.group(1) == 12
        if matches.group(6) == "PM":
            matches.group(4) == int(matches.group(4))+12
        if None in matches.groups():
            return (f"{matches.group(1)}:00 to {matches.group(4)}:00")
        else:
            return (f"{matches.group(1)}{matches.group(2)} to {matches.group(4)}{matches.group(5)}")


if __name__ == "__main__":
    main()
