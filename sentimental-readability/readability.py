from cs50 import get_string


# get text input
t = get_string("Text: ")


#calculate letters
l = 0
for i in range(len(t)):
    if ((ord(t[i]) > 64 and ord(t[i]) < 91) or (ord(t[i]) > 96 and ord(t[i]) < 123)):
        l += 1


# calculate words
w = 0
for j in range(len(t)):
    if (ord(t[j]) == 32):
        w += 1


# calculate sentences
s = 0
for i in range(len(t)):
    if ((ord(t[i]) > 64 and ord(t[i]) < 91) or (ord(t[i]) > 96 and ord(t[i]) < 123)):
        l += 1


# calculate grade level
L = 0
S = 0
n = (0.0588 * L) - (0.296 * S) - 15.8
n = round(n)


# print grade level
if (n < 1):
    print("Before Grade 1")
elif (n >= 16):
    print("Grade 16+")
else:
    print(f"Grade {n}")