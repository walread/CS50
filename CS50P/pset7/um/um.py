import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if match := re.findall(r"(?![a-z])um(?![a-z])", s.lower()):
        return len(match)


if __name__ == "__main__":
    main()
