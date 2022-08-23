def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) > 6:
        return False
    else:
        if s[0:1].isalpha():
            if s.isalnum:
                t = ""
                for c in s:
                    if c.isdigit():
                        t += c
                if t.isdigit():
                    return True
            else:
                return True
        else:
            return False


main()