import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w*)"', s):
        return (f"https://youtu.be/{matches.group}")


if __name__ == "__main__":
    main()
