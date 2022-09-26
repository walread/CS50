import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if match == None:
        raise ValueError
    else:
        start = int(match.group(1))
        end = int(match.group(4))
        if match.group(3) == "PM" and start != 12:
            start = start+12
        elif start == 12:
            start = 0
        if match.group(6) == "PM" and start != 12:
            end = end+12
        elif end == 12:
            end = 0
        if None in match.groups():
            return (f"{start:02}:00 to {end:02}:00")
        else:
            return (f"{start:02}{match.group(2)} to {end:02}{match.group(5)}")


if __name__ == "__main__":
    main()
