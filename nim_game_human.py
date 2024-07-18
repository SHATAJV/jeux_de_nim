#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim (variante simple et de Marienbad)

"""

def play(player1, player2,current_player):

    pile = 21
    if current_player==player1:
      print(f"it's your turn{player1}")
    else:
        print(f"it's your turn {player2}")
    while True :
         print(f"there is {pile} piles")
         choice= input((f"Enter How many piles you want to take(1_4):"))
         try:
             if 1<choice<=4  and choice<=pile :

                break
             else:
                 print("you didn't enter right choice please right again")
         except ValueError:
             print(f"Error ! try again")
    pile -= choice
    if pile==0:
        print(f"You Loose {current_player}!")


def main():
    player1 = input("Enter Your name: ")
    player2 = input("Enter Your name: ")
    current_player = input("who want to start game(enter the name): ").strip().lower()
    winner= play(player1, player2,current_player)
    print(winner)

if __name__ == "__main__":
    main()
