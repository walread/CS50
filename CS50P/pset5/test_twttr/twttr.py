def main():
    s = input("Input: ")
    print("Output:", shorten(s))


def shorten(word):
    vowel = "aeiou"
    for c in vowel:
        word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()
