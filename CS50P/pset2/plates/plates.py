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
                    t, u = s.split(c)
                    break
            if u.isdigit() or len(u) == 0:
                return True
        else:
            return False
    else:
        return False


main()