from cs50 import get_string

s = get_string("Number: ")
if (int(s[0]) == 3):
    if (int(s[1]) == 4 or int(s[1]) == 7):
        if (len(s) == 15):
            print("AMEX")
elif (int(s[0]) == 5):
    if (int(s[1]) == 1 or int(s[1]) == 2 or int(s[1]) == 3 or int(s[1]) == 4 or int(s[1]) == 5):
        if (len(s) == 16):
            print("MASTERCARD")
elif (int(s[0]) == 4):
    if (len(s) == 13 or len(s) == 16):
        print("VISA")
else:
    print(")