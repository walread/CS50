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
        if s.isalnum():
            if s[0:1].isalpha:
                for c in s:
                    if c.isdigit():
                        s, t = s.split(c)
                        break
                if t.isdigit():
                    return True
            else:
                return False
        else:
            return False
    return True


main()