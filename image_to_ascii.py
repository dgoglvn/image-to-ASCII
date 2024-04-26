# image_to_ascii v1.0

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()
target_image = Path(args.path)

# Levels of gray
gradient = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gradient_length = len(gradient)

# Open the input file
try:
    image = Image.open(target_image)
    print("Image was found and opened!")
except FileNotFoundError as e:
    print("Invalid input file!")
    quit()

# Print the size of the original image
print(f"\nOriginal size: {image.size}")

# Resize the image
DEFAULT_SIZE = 250
image.thumbnail((DEFAULT_SIZE, DEFAULT_SIZE))
# Print the size of the new image
print(f"\nNew size: {image.size}")

# Convert image to grayscale
image = image.convert("L")

width, height = image.size
output_image = Image.new("RGB", (width * 10, height * 10), color="white")
draw = ImageDraw.Draw(output_image)
# Load monospace font
font = ImageFont.truetype("~/library/fonts/RobotoMono-Regular.ttf", 12)

# Convert int to char
for y in range(height):
    for x in range(width):
        # Get the brightness value
        brightness = image.getpixel((x, y))
        # Map the brightness value to the gradient index
        index = int(brightness / 255 * (gradient_length - 1))
        char = gradient[index]
        # Draw the character at the corresponding position
        draw.text((x * 10, y * 10), char, font=font, fill=(0, 0, 0))

output_image.show()
output_image.save("girl_with_a_pearl_earring_ascii.jpg")