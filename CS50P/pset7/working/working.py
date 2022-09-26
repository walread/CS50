import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if match == None:
        raise ValueError
    else:
        if match.group(3) == "PM":
            match.group(1) == int(match.group(1))+12
        if match.group(6) == "PM":
            match.group(4) == int(match.group(4))+12
        if None in match.groups():
            return (f"{match.group(1)}:00 to {match.group(4)}:00")
        else:
            return (f"{match.group(1)}{match.group(2)} to {match.group(4)}{match.group(5)}")


if __name__ == "__main__":
    main()
