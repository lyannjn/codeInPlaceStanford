"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    while True:
        hailstones()


def hailstones():
    num = int(input("Enter a number: "))
    steps = 0
    while num != 1:
        first_num = num
        # Even number
        if num % 2 == 0:
            num = num // 2
            print(str(first_num) + " is even, so I take half: " + str(num))
        # Odd number
        else:
            num = (num * 3) + 1
            print(str(first_num) + " is odd, so I make 3n + 1: " + str(num))
        steps += 1
    print("This process took " + str(steps) + " steps to reach 1")
    print("")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
