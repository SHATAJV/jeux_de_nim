#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim ( Compelet)
"""
import random
def main():
    print(f"Welcome to Nim Games")
    type_gmame= input("Enter de type de game witch you want play(2players, 1player, Marienband:").strip()
    if type_gmame== "2players":
        def play_2players(player1, player2, current_player):
            pile = 21

            while pile > 0:
                print(f"\nThere are {pile} matches left.")
                if current_player == player1:
                    print(f"It's your turn, {player1}")
                else:
                    print(f"It's your turn, {player2}")

                while True:
                    try:
                        choice = int(input("How many matches do you want to take (1-4)? "))
                        if 1 <= choice <= 4 and choice <= pile:
                            break
                        else:
                            print(
                                "Invalid choice. Please enter a number between 1 and 4 and not more than the remaining matches.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                pile -= choice
                if pile == 0:
                    print(f"{current_player} took the last match and lost!")
                    return

                # Switch current player
                current_player = player2 if current_player == player1 else player1

        def main_2player():
            player1 = input("Enter the name of player 1: ")
            player2 = input("Enter the name of player 2: ")
            current_player = input("Who wants to start the game? (enter the name): ").strip()

            play_2players(player1, player2, current_player)
    elif type_gmame== "1player":
        def play_1player(user, current_player):
            pile = 21

            while pile > 0:
                print(f"\nThere are {pile} matches left.")
                if current_player == user:
                    print(f"It's your turn, {user}")
                    while True:
                        try:
                            choice = int(input("How many matches do you want to take (1-4)? "))
                            if 1 <= choice <= 4 and choice <= pile:
                                break
                            else:
                                print(
                                    "Invalid choice. Please enter a number between 1 and 4 and not more than the remaining matches.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                else:
                    print("It's the computer's turn")
                    if pile % 5 == 0:
                        choice = random.randint(1, 4)
                    else:
                        choice = pile % 5
                    print(f"Computer takes {choice} matches")

                pile -= choice
                if pile == 0:
                    print(f"{current_player} took the last match and lost!")
                    return

                # Switch current player
                if current_player == user:
                    current_player = "Computer"
                else:
                    current_player = user

        def main_1player():
            user = input("Enter the name of the player: ")
            current_player = input("Who wants to start the game? (enter the name or 'Computer'): ").strip()

            if current_player not in [user, "Computer"]:
                print("Invalid name for the starting player. Please restart the program and enter a valid name.")
                return
              play_1player(user, current_player)
    else:
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
                        choice = int(input(
                            f"How many matches do you want to take from pile {pile_index} (1-{piles[pile_index]})? "))
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

        def main_Marienband():
            player1 = input("Enter the name of player 1: ")
            player2 = input("Enter the name of player 2: ")
            current_player = input("Who wants to start the game? (enter the name): ").strip()

            play_marienbad(player1, player2, current_player)
if __name__ == "__main__":
    main()