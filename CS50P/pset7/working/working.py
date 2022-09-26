import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if match == None:
        raise ValueError
    else:
        start = match.group(1)
        end = match.group(4)
        if match.group(3) == "PM":
            start = int(start)+12
        if match.group(6) == "PM":
            end = int(end)+12
        if None in match.groups():
            return (f"{start:02}:00 to {end}:00")
        else:
            return (f"{start}{match.group(2)} to {end}{match.group(5)}")


if __name__ == "__main__":
    main()
