def main():
    height = get_height()
    for i in range(height):
        for j in range(height)
        print("#")

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                break
        except ValueError:
            print("That is not an integer!")
    return n

main()