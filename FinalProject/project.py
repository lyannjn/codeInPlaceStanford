"""
File: project.py
Coded by: Lyann Jafif Nahmias
-----------------------------
This program randomly generates simple binary operation problems for the user,
(1-digit integers (i.e., the numbers 0 through 9 or even 10))
reads in the answer from the user, and then checks to see
if they got it right or wrong, until the user appears to
have mastered the material.
(The program keeps giving the user problems until the user
has gotten a definite number of problems correct in a row)
A patch of an image prints every correct answer until the user has got
all the correct answers (which shows the complete image).
The patch changes color every time (filter)
"""

from simpleimage import SimpleImage
from PIL import Image
import random
import operator
import time


DEFAULT_FILE = 'images/awesomeness.jpg'
N_ROWS = 2
N_COLS = 3

MIN_CORRECT_ANSWERS_ROW = N_ROWS * N_COLS
# Range of numbers for problems
MIN = 0
MAX = 10

image = SimpleImage(DEFAULT_FILE)
WIDTH = image.width
HEIGHT = image.height
RELATIVE_WIDTH = WIDTH // N_COLS
RELATIVE_HEIGHT = HEIGHT // N_ROWS


def main():
    print("What Binary Operation would you like to practice?")
    options = ["1: Addition", "2: Subtraction", "3: Multiplication"]
    print(*options, sep='\n')
    users_select = int(input("Your answer: "))
    if users_select == 1:
        op = "+"
    elif users_select == 2:
        op = "-"
    else:
        op = "*"
    binary_operations(op)


def binary_operations(op_str):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    op_names = {"+": "addition", "-": "subtraction", "*": "multiplication"}
    op = ops[op_str]
    counter = 0
    while counter != MIN_CORRECT_ANSWERS_ROW:
        random_num1 = random.randint(MIN, MAX)
        random_num2 = random.randint(MIN, MAX)
        correct_ans = op(random_num1, random_num2)
        print("What is " + str(random_num1) + op_str + str(random_num2) + "?")
        users_mult = int(input("Your answer: "))
        if correct_ans == users_mult:
            counter += 1
            print("Correct! You've gotten " + str(counter) + " correct in a row.")

            # A patch of the image prints every correct answer until the user has got
            # all the correct answers which shows the complete image
            final_image = SimpleImage.blank(WIDTH, HEIGHT)
            add_image(final_image, counter)
            final_image.show()
            time.sleep(1)


            if counter == MIN_CORRECT_ANSWERS_ROW:
                print("Congratulations!!! You mastered " + op_names[op_str])
        else:
            print("Incorrect. The expected answer is " + str(correct_ans))
            counter = 0


def add_image(final_image, counter):
    rows = (counter - 1) // N_COLS
    for row in range(rows+1):
        cols = N_COLS if (counter >= (row + 1) * N_COLS) else (((counter - 1) % N_COLS) + 1)
        for col in range(cols):
            patch = make_recolored_patch(random.uniform(0, 2), random.uniform(0, 2), random.uniform(0, 2))
            patch = trim(patch, row, col)
            add_patch(final_image, row, col, patch)


def trim(patch, row, col):
    trimmed_image = SimpleImage.blank(RELATIVE_WIDTH, RELATIVE_HEIGHT)
    width = patch.width // N_COLS
    height = patch.height // N_ROWS
    for y in range(height):
        for x in range(width):
            pixel = patch.get_pixel(x + (col * RELATIVE_WIDTH), y + (row * RELATIVE_HEIGHT))
            trimmed_image.set_pixel(x, y, pixel)
    return trimmed_image


def add_patch(image, row, col, patch):
    for y in range(RELATIVE_HEIGHT):
        for x in range(RELATIVE_WIDTH):
            pixel = patch.get_pixel(x, y)
            image.set_pixel(x + (col * RELATIVE_WIDTH), y + (row * RELATIVE_HEIGHT), pixel)


def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(DEFAULT_FILE)
    for pixel in patch:
        pixel.red = red_scale * pixel.red
        pixel.green = green_scale * pixel.green
        pixel.blue = blue_scale * pixel.blue
    return patch


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()