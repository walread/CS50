import sys

input_file, input_type = sys.argv[1].lower().split(".")
output_file, output_type = sys.argv[2].lower().split(".")

types = ["jpg", "jpeg", "png"]

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif input_type not in types:
    sys.exit("Invalid input")
elif output_type not in types:
    sys.exit("Invalid output")
elif input_type != output_type:
    sys.exit("Input and output have different extensions")

try:

except FileNotFoundError:
    sys.exit("Input does not exist")
