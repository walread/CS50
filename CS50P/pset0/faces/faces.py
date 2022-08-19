def main():
    input = ("Input: ")

    print(emoji(input))

# define emoji function
def emoji(str):
    if ":)" in str:
        str = str.replace(":)", "🙂")
    elif ":(" in str:
        str = str.replace(":(", "🙁")
    else:
        str = str

# call main function
main()