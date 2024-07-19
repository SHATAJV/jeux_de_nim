#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Nim Game (Complete) This script implements three versions of the Nim game:
 1. **Two-Player Nim**: A game where two players take turns removing matches from a single pile. The player who takes the last match loses.
 2. **Single-Player Nim**: A game where a player competes against the computer. The rules are similar to the two-player game, but the computer takes turns making moves as well. The player who takes the last match loses.
  3. **Marienbad**: A variant of Nim played with multiple piles. Players take turns removing matches from one pile.
   The player who takes the last match loses.
    Game Types: - **2players**: Play against another human player.
     **1player**: Play against the computer.
      **Marienband**: Play the Marienbad variant with multiple piles.
"""

import random


def main():
    """
    Main function to start the Nim game based on the selected game type.
    """
    print("Welcome to Nim Games")
    print("Game Types: ")
    print("**2players**: Play against another human player.")
    print("**1player**: Play against the computer.")
    print("**Marienband**: Play the Marienbad variant with multiple piles.")


    valid_game_types = ["2players", "1player", "Marienband"]

    while True:
        type_game = input("Enter the type of game you want to play (2players, 1player, Marienband): ").strip()
        if type_game in valid_game_types:
            break
        else:
            print("Invalid game type. Please enter a valid game type.")

    if type_game == "2players":

        def play_2players(player1, player2, current_player):
            """
            Play the 2-player version of the Nim game.

            Args:
                player1 (str): Name of player 1.
                player2 (str): Name of player 2.
                current_player (str): Name of the current player.
            """
            pile = 21

            while pile > 0:
                print(f"\nThere are {pile} matches left.")
                print(f"It's your turn, {current_player}")

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
            """
            Initialize and start the 2-player version of the Nim game.
            """
            player1 = input("Enter the name of player 1: ")
            player2 = input("Enter the name of player 2: ")
            current_player = input("Who wants to start the game? (enter the name): ").strip()

            play_2players(player1, player2, current_player)

        main_2player()

    elif type_game == "1player":

        def play_1player(user, current_player):
            """
            Play the 1-player version of the Nim game against the computer.

            Args:
                user (str): Name of the user.
                current_player (str): Name of the current player (user or Computer).
            """
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
                current_player = "Computer" if current_player == user else user

        def main_1player():
            """
            Initialize and start the 1-player version of the Nim game.
            """
            user = input("Enter the name of the player: ")
            current_player = input("Who wants to start the game? (enter the name or 'Computer'): ").strip()

            if current_player not in [user, "Computer"]:
                print("Invalid name for the starting player. Please restart the program and enter a valid name.")
                return

            play_1player(user, current_player)

        main_1player()

    elif type_game == "Marienband":

        def play_marienbad(player1, player2, current_player):
            """
            Play the Marienbad version of the Nim game.

            Args:
                player1 (str): Name of player 1.
                player2 (str): Name of player 2.
                current_player (str): Name of the current player.
            """
            piles = [1, 3, 5, 7]

            while sum(piles) > 0:
                print(f"\nCurrent piles: {piles}")
                print(f"It's your turn, {current_player}")

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

                # Switch current player
                current_player = player2 if current_player == player1 else player1

        def main_marienbad():
            """
            Initialize and start the Marienbad version of the Nim game.
            """
            player1 = input("Enter the name of player 1: ")
            player2 = input("Enter the name of player 2: ")
            current_player = input("Who wants to start the game? (enter the name): ").strip()

            play_marienbad(player1, player2, current_player)

        main_marienbad()


if __name__ == "__main__":
    main()
