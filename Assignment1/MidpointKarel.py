from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
MidpointKarel leaves a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel puts down additional beepers as it
looks for the midpoint, but picks them up again before it
stops. It is assumed that the world is at least as tall as it is wide.
"""

"""
Solution programmed by: 
Lyann Jafif Nahmias
-----------------------
Program runs in the following worlds:
MidpointKarel.w (default world)
MidpointFindingKarel.w
Midpoint1.w
Midpoint2.w
Midpoint8.w
"""

"""
main() explanation
------------------
Karel first puts beepers all over the world following a spiral path,
ending up in the center of the world.
Karel then moves downwards to the midpoint and paints it red.
Karel is moved back to the initial corner and then removes 
all the beepers in the world except the one in the midpoint,
where only the paint is removed.
"""


def main():
    # This `if` is only to account for the 1x1 world
    if front_is_blocked():
        put_beeper()
    else:
        spiral_put_beepers()
        paint_midpoint()
        back_to_1x1_position()
        remove_unpainted_beepers()


def spiral_put_beepers():
    do_curve()
    # Pre-condition: Karel is placed in a corner WITHOUT beepers present
    # Post-condition: Karel is placed in the spiral's center corner after
    # the last possible curve was done and beeper put
    while no_beepers_present():
        do_curve()


def do_curve():
    put_beeper()
    move()
    safe_beeper()
    initial_curve_position()
    check_for_next_curve()


def safe_beeper():
    # Pre-condition: Karel is placed in a corner WITHOUT beepers present
    # Post-condition: Karel is placed in a corner WITH beepers present
    while no_beepers_present():
        if front_is_clear():
            put_beeper()
            move()
        # Karel moves to next edge to form the complete curve
        else:
            turn_left()


def initial_curve_position():
    rotate_180deg()
    move()


def check_for_next_curve():
    turn_right()
    move()


def paint_midpoint():
    face_south()
    # Pre-condition: Karel is placed in the spiral's center corner facing South
    # Post-condition: Karel is in the first row facing a wall
    while front_is_clear():
        move()
    paint_corner(RED)


def face_south():
    if facing_north():
        rotate_180deg()
    if facing_east():
        turn_right()
    if facing_west():
        turn_left()


def back_to_1x1_position():
    turn_right()
    safe_move()
    rotate_180deg()


def safe_move():
    while front_is_clear():
        move()


def remove_unpainted_beepers():
    # Pre-condition: Karel is facing East standing in the first beeper
    # Post-condition: Karel leaves the midpoint beeper (unpainted)
    # standing in the last corner after cleaning the world
    while beepers_present():
        if corner_color_is(RED):
            paint_corner(BLANK)
        else:
            pick_beeper()
        if front_is_clear():
            move()
        else:
            move_to_next_line()


def move_to_next_line():
    rotate_180deg()
    safe_move()
    turn_right()
    if front_is_clear():
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def rotate_180deg():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
