# main function
def main():
    n = get_height()
    for i in range(n):
        for j in range()
            print()
        for k in range(i + 1):
            print("#", end="")
        print()

# height input function
def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                break
        except ValueError:
            print("That is not an integer!")
    return n

# call main
main()