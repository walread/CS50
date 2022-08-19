def main():
    string = input("Input: ")

    emoji(string)

# define emoji function
def emoji(str):
    if ":)" in str:
        print(str.replace(":)", "🙂"))
    if ":(" in str:
        print(str.replace(":(", "🙁"))
    else:
        print(str)

# call main function
main()