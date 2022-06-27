def main():
    n = get_height()
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()


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