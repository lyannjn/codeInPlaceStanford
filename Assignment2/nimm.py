"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China.
Players alternate taking stones until there are zero left.
The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""

START_NUM_STONES = 20


def main():
    counter = START_NUM_STONES
    print("There are " + str(counter) + " stones left")
    # Tu avoid a fencepost error we start with the first player's turn
    player_turn = 1
    select = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones?"))
    # To correct the input of an invalid number
    while select != 1 and select != 2:
        select = int(input(" Please enter 1 or 2:"))
    print(" ")
    counter -= select
    # Next player's turn, then the while loop begins until there is a winner
    player_turn = 2
    while counter > 0:
        if counter > 1:
            print("There are " + str(counter) + " stones left")
            select = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones?"))
            # To correct the input of an invalid number
            while select != 1 and select != 2:
                select = int(input(" Please enter 1 or 2:"))
            print(" ")
            counter -= select
        # No need to ask the question if there is only 1 stone left
        # (the last player must remove the last stone)
        else:
            print("There is only " + str(counter) + " stone left")
            counter -= select
        # To change the turn of the player
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
    print("Player " + str(player_turn) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
