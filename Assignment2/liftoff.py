"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""
import time
COUNTDOWN = 10


def main():
    for i in range(COUNTDOWN):
        print(COUNTDOWN - i)
        time.sleep(0.5)
    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
