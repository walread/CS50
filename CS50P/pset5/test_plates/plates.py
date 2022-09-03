def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not s.isalnum():
        return False
    elif not s[0:1].isalpha():
        return False
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            t, u = s.split(c, maxsplit=1)
            if not u.isdigit() and len(u) > 0:
                return False
            else:
                break
    return True


if __name__ == "__main__":
    main()
