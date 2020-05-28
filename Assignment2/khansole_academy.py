"""
File: khansole_academy.py
-------------------------
This program randomly generates simple addition problems for the user,
(2-digit integers (i.e., the numbers 10 through 99))
reads in the answer from the user, and then checks to see
if they got it right or wrong, until the user appears to
have mastered the material.
(The program keeps giving the user problems until the user
has gotten 3 problems correct in a row)
"""

import random
MIN_CORRECT_ANSWERS_ROW = 3
# Range for addition problems
MIN = 10
MAX = 99


def main():
    counter = 0
    while counter != MIN_CORRECT_ANSWERS_ROW:
        random_num1 = random.randint(MIN, MAX)
        random_num2 = random.randint(MIN, MAX)
        correct_sum = random_num1 + random_num2
        print("What is " + str(random_num1) + " + " + str(random_num2) + "?")
        users_sum = int(input("Your answer: "))
        if correct_sum == users_sum:
            counter += 1
            print("Correct! You've gotten " + str(counter) + " correct in a row.")
            if counter == MIN_CORRECT_ANSWERS_ROW:
                print("Congratulations!!! You mastered addition")
        else:
            print("Incorrect. The expected answer is " + str(correct_sum))
            counter = 0


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
