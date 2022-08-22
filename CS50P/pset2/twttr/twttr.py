input = input("Input: ")

for i in len(input):
    if input[i].upper() == "A" or input[i].upper() == "E" or input[i].upper() == "I" or input[i].upper() == "O" or input[i].upper() == "U":
        input = input[i].replace("")

print("Output:", input)