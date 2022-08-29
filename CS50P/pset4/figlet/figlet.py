from pyfiglet import Figlet
import sys

if len(sys.argv) == 1:
elif len(sys.argv) == 3:
    f = sys.argv[1]
    s = sys.argv[2]
    figlet = Figlet()
    if f not in figlet.getFonts():
        sys.exit("Font not in font list")
    else:
        figlet.setFont(font = f)
        print(figlet.renderText(s))
else:
    