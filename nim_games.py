import random

def play(user, current_player):
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
                        print("Invalid choice. Please enter a number between 1 and 4 and not more than the remaining matches.")
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

def main():
    user = input("Enter the name of the player: ")
    current_player = input("Who wants to start the game? (enter the name or 'Computer'): ").strip()

    if current_player not in [user, "Computer"]:
        print("Invalid name for the starting player. Please restart the program and enter a valid name.")
        return

    play(user, current_player)

if __name__ == "__main__":
    main()

