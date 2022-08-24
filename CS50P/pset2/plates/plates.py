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
    for c in s:
        if c.isdigit():
            t, u = s.split(c)
            if u.isdigit:
                return True
            else:
                return False
    return True


main()