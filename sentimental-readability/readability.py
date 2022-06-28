from cs50 import get_string


# get text input
t = get_string("Text: ")


#calculate grade level
L = len(t)
S =
n = (0.0588 * L) - (0.296 * S) - 15.8
n = round(n)


# print grade level
if (n < 1):
    print("Before Grade 1")
elif (n >= 16):
    print("Grade 16+")
else:
    print(f"Grade {n}")