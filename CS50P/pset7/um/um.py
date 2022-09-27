import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if match := re.findall(r"( um )?", s.lower()):
        return len(match.groups())


if __name__ == "__main__":
    main()
