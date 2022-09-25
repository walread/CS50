import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s):
        return (f"{matches.group(1)}{matches.group(2)} to {matches.group(4)}{matches.group(5)}")


if __name__ == "__main__":
    main()
