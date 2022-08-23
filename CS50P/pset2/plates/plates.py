def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) <= 6:
        if s[0:1].isalpha():
            t = ""
            for c in s:
                if c.isdigit():
                    t += c
            if t.isdigit() or len(t) == 0:
                return True
        else:
            return False
    else:
        return False


main()