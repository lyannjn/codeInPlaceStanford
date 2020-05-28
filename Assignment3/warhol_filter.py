"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/Diseño sin título.png'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # I wanted to use a specific list of colors and repeat them if the canvas size is bigger
    colored_images = [pink_patch(), green_patch(), yellow_patch(), red_patch(), blue_patch(), indigo_patch()]
    for i in range(N_ROWS):
        for j in range(N_COLS):
            # Loops the default_color_list positions to obtain the correspondent color
            # The module % helps repeat the process from position [0] to [5] no matter the N_COLS and rows
            image = colored_images[((i * N_COLS) + j) % len(colored_images)]
            insert_patch(i, j, image, final_image)
    final_image.show()


def insert_patch(i, j, image, added_image):
    # Inserts the colored patch (image) to in the
    # correct next position of the canvas (added_image) from left to right in each row
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            pixel = image.get_pixel(x, y)
            added_image.set_pixel(x + (j * PATCH_SIZE), y + (i * PATCH_SIZE), pixel)


def pink_patch():
    return make_recolored_patch(1.4, .8, 1.4)

def green_patch():
    return make_recolored_patch(.9, 1.55, .9)

def yellow_patch():
    return make_recolored_patch(1.5, 1.5, 0)

def red_patch():
    return make_recolored_patch(1.55, .9, .9)

def indigo_patch():
    return make_recolored_patch(.9, .9, 1.55)

def blue_patch():
    return make_recolored_patch(0.30, 1.44, 2.55)


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch


if __name__ == '__main__':
    main()