from cs50 import get_string


# get text input
s = get_string("Text: ")


#calculate grade level
n = 2.6


# print grade level
if (n < 1):
    print("Before Grade 1")
elif (n >= 16):
    print("Grade 16+")
else:
    print(f"Grade {n}")