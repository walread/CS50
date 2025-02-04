from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(font_list)
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    e = sys.argv[1]
    f = sys.argv[2]
    if e != "-f":
        sys.exit("Invalid usage")
    elif f not in font_list:
        sys.exit("Invalid usage")
    else:
        s = input("Input: ")
        figlet.setFont(font=f)
        print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")
