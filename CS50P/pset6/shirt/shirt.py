import sys
from PIL import Image, ImageOps
import PIL

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

shirt = Image.open("shirt.png")
size = shirt.size

try:
    with Image.open(sys.argv[1]) as photo:
        sized_photo = ImageOps.fit(photo, size)
except FileNotFoundError:
    sys.exit("Input does not exist")

sized_photo.paste(shirt, shirt)
sized_photo.save(sys.argv[2])

shirt.close()
