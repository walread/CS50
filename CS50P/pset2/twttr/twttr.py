input = input("Input: ")

vowel = "AEIOUaeiou"

for c in vowel:
    input = input.replace(c, "")

print("Output:", input)