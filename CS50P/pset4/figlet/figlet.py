from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(font_list)
    figlet.setFont(font = f)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    s = input("Input: ")
    f = sys.argv[2]
    if f not in font_list:
        sys.exit("Font not in font list")
    else:
        figlet.setFont(font = f)
        print(figlet.renderText(s))
else:
    sys.exit
