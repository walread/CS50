import sys

input_file, input_type = sys.argv[1].split(".")
output_file, output_type = sys.argv[2].split(".")

print(input_type)
print(output_type)

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif input_type != "jpg" or input_type != "jpeg" or input_type != "png":
    sys.exit("Invalid input")
elif output_type != "jpg" or output_type != "jpeg" or output_type != "png":
    sys.exit("Invalid output")
elif input_type != output_type:
    sys.exit("Input and output have different extensions")
