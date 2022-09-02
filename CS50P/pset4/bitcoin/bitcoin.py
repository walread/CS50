import requests
import sys

if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = r.json()["bpi"]["USD"]["rate"]
    print(f"${rate * int(sys.argv[1])}") 
except requests.RequestException:
    sys.exit("Decoding fail")
