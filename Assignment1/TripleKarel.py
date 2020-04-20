from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
TripleKarel is able to paint the exterior of three 
buildings in a given world, as described in the 
Assignment 1 handout
"""

"""
Solution programmed by: 
Lyann Jafif Nahmias
-----------------------
Program runs in the following worlds:
TripleKarel.w (default world)
Triple1.w
Triple2.w
Triple3.w
"""


def main():
    # Karel paints the first two buildings
    for i in range(2):
        paint_a_building()
    # Karel paints the last of the three buildings in the world
    paint_two_sides()
    safe_side_painting()


# Karel paints the three sides in a single building
def paint_a_building():
    paint_two_sides()
    paint_side_until_front_is_blocked()


def paint_two_sides():
    for i in range(2):
        paint_side()


def paint_side():
    # Pre: Karel is in the beginning of a building's side
    safe_side_painting()
    # Post: Karel faces the next side of the building
    turn_left()
    move()


def safe_side_painting():
    # Pre-condition: there is a wall (building) in Karel's left
    # Post-condition: there is NO wall in Karel's left
    while left_is_blocked():
        put_beeper()
        move()


def paint_side_until_front_is_blocked():
    # Pre-condition: Karel's front is clear
    # Post-condition: Karel is facing a wall
    while front_is_clear():
        put_beeper()
        move()
    # Karel is positioned in the beginning of the next building's side
    # Parallel direction of the wall
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
