from cs50 import get_string

s = get_string("Number: ")
n = int(s)
if (n):
    print("AMEX")
elif (n):
    print("MASTERCARD")
elif (n):
    print("VISA")
else:
    print("INVALID")