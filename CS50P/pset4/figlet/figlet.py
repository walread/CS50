from pyfiglet import Figlet
import sys

if len(sys.argv) != 3:
    sys.exit
else:
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font=f)
