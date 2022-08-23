def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for c in s:
        if c.isalpha() or c.is

    if len(s) != 6:
        return False
    else:
        return True


main()