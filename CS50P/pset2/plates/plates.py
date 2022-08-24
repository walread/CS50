def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# must be 2-6 characters, all alphanumeric
# characters 1-2 must be alpha
# if there a numbers, letters must not follow

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
    else:
        return True

main()