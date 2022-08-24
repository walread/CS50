def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# use while true loop to split string (while string contains digits, split string)
# could try to insert space once number is reached to split string without loosing first number
# break while loop once first number is reached
# use try, except, else to overcome assignment error when spliting

def is_valid(s):

    if len(s) > 6 or len(s) < 2:
        return False
    elif not s.isalnum:
        return False
    elif not s[0:1].isalpha():
        return False
    for c in len(s):
        if s[c].isdigit():
            if s[c] == "0":
                return False
            t, u = s.split(s[c])
            if not u.isdigit() and len(u) > 0:
                return False
            else:
                break
    return True


main()