#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim ( Marienbad)
"""
def play(player1, player2, current_player):
    pile = [1,3,5,7]

    while sum(pile) > 0:
        print(f"\nThere are {pile} matches left.")
        if current_player == player1:
            print(f"It's your turn, {player1}")
        else:
            print(f"It's your turn, {player2}")

        while True:
            try:
                choice = int(input("How many matches do you want to take (1-3)? "))
                if 1 <= choice <= 4 and choice <= pile:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4 and not more than the remaining matches.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        pile[] -= choice
        if pile == 0:
            print(f"{current_player} took the last match and lost!")
            return

        # Switch current player
        current_player = player2 if current_player == player1 else player1

def main():
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    current_player = input("Who wants to start the game? (enter the name): ").strip()



    play(player1, player2, current_player)

if __name__ == "__main__":
    main()

