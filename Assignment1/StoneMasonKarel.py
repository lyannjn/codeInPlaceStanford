from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
StoneMasonKarel solves the "repair the quad" problem from 
Assignment 1. Karel supports the four arches of the world 
with beepers.
"""

"""
Solution programmed by: 
Lyann Jafif Nahmias
-----------------------
Program runs in the following worlds:
StoneMasonKarel.w (default world)
SampleQuad1.w
SampleQuad2.w
"""


def main():
    support_three_arches()
    # Support the last arch
    complete_arch()


def support_three_arches():
    # Pre-condition: Karel is facing East in the bottom of the arch
    # Post-condition: Karel is facing East in the bottom of the next unchecked arch
    for i in range(3):
        complete_arch()
        go_down()
        move_to_next_arch()


def complete_arch():
    # To turn North
    turn_left()
    repair_arch()
    # To prevent a fencepost bug
    safe_beeper()


def repair_arch():
    # Pre-condition: Karel is facing North with no wall in front
    # Post-condition: Karel is standing in the last unchecked corner at the top of the arch
    while front_is_clear():
        safe_beeper()
        move()


def safe_beeper():
    if no_beepers_present():
        put_beeper()


def go_down():
    # Karel turns South
    rotate_180deg()
    # Pre-condition: Karel is at the top of the arch facing South
    # Post-condition: Karel is facing East in the bottom of the arch
    while front_is_clear():
        move()
    turn_left()


def move_to_next_arch():
    for i in range(4):
        move()


def rotate_180deg():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
