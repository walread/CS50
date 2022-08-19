def main():
    string = input("Input: ")

    print(emoji(string))

# define emoji function
def emoji(str):
    if ":)" in str:
        str = str.replace(":)", "🙂")
    if ":(" in str:
        str = str.replace(":(", "🙁")
    else:
        str = str

# call main function
main()