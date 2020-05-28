"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

# The line below imports SimpleImage for use here
# It depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'


def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    for pixel in image:
        codeinplace_filter(pixel)

    # Show the image after the transform
    image.show()
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


def codeinplace_filter(pixel):
    # To apply the Code in Place filter,
    # change every ​pixel​ to have the following
    # new red green and blue values
    R = pixel.red
    G = pixel.green
    B = pixel.blue
    pixel.red = R * 1.5
    pixel.green = G * 0.7
    pixel.blue = B * 1.5


if __name__ == '__main__':
    main()