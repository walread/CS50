import sys

input_file, input_type = sys.argv[1].split(".")
input_file, input_type = sys.argv[2].split(".")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

