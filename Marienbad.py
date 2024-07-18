#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim ( Marienbad)
"""
def play_marienbad(player1, player2, current_player):
    piles = [1, 3, 5, 7]

    while sum(piles) > 0:
        print(f"\nCurrent piles: {piles}")
        if current_player == player1:
            print(f"It's your turn, {player1}")
        else:
            print(f"It's your turn, {player2}")

        while True:
            try:
                pile_index = int(input(f"{current_player}, from which pile do you want to take (0-3)? "))
                if 0 <= pile_index < len(piles) and piles[pile_index] > 0:
                    break
                else:
                    print("Invalid pile choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                choice = int(input(f"How many matches do you want to take from pile {pile_index} (1-{piles[pile_index]})? "))
                if 1 <= choice <= piles[pile_index]:
                    break
                else:
                    print("Invalid number of matches. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        piles[pile_index] -= choice
        if sum(piles) == 0:
            print(f"{current_player} took the last match and lost!")
            return

        current_player = player2 if current_player == player1 else player1

def main():
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    current_player = input("Who wants to start the game? (enter the name): ").strip()



    play_marienbad(player1, player2, current_player)

if __name__ == "__main__":
    main()


