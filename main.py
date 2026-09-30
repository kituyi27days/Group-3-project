"""
Player Attack System

Purpose:  
The purpose of the player attack system is to allow the player to choose a position on the opponents board to attack and determine whether the attack is a hit or a miss.

Inputs:  
- Row chosen by the player  
- Column chosen by the player  
- Opponent’s board  
- Previous attack locations  

Steps:  
1. Ask the player to enter a row and column to attack.  
2. Check that the chosen position is inside the board.  
3. Check that the player has not already attacked that position.  
4. Check whether there is a ship at the chosen position.  
5. Record the attack as either a hit or a miss.  
6. Update the board and save the attacked position.

Data needed:  
- The opponent’s board  
- A list of previous attacks  
- The row and column chosen by the player  
- Values used to represent ships, hits, misses, and empty spaces
"""
BOARD_SIZE = 10
SHIP = "S"
HIT = "X"
MISS = "O"

# Stores coordinates the player has already attacked
previous_attacks = []

#Function to get the attack coordinates from the player and validate them
def get_attack_coordinates():

    attack_row = int(input("Enter the row you want to attack between 0 and 9 (inclusive): "))
    attack_column = int(input("Enter the column you want to attack between 0 and 9 (inclusive): "))

    flag = False

    while flag == False:

        if attack_row < 0 or attack_row >= BOARD_SIZE:
            print("Invalid row. Please enter a value between 0 and 9.")

            attack_row = int(input("Enter the row you want to attack between 0 and 9 (inclusive): "))

        elif attack_column < 0 or attack_column >= BOARD_SIZE:
            print("Invalid column. Please enter a value between 0 and 9.")

            attack_column = int(input("Enter the column you want to attack between 0 and 9 (inclusive): "))

        else:
            flag = True

    return attack_row, attack_column

#Function to check if the player has already attacked the chosen position
def already_attacked(attack_row, attack_column, previous_attacks):

    if [attack_row, attack_column] in previous_attacks:
        return True

    else:
        return False

#Function to store the attack coordinates in the previous_attacks list
def record_attack(attack_row, attack_column, previous_attacks):

    previous_attacks.append([attack_row, attack_column])

#Function to handle the player's attack on the opponent's board
def player_attack(board, previous_attacks):

    valid_attack = False

    while valid_attack == False:

        attack_row, attack_column = get_attack_coordinates()

        if already_attacked(attack_row, attack_column, previous_attacks):
            print("You already attacked this location. Choose another location.")

        else:
            record_attack(attack_row, attack_column, previous_attacks)

            if board[attack_row][attack_column] == SHIP:
                board[attack_row][attack_column] = HIT
                print("Hit!")

            else:
                board[attack_row][attack_column] = MISS
                print("Miss!")

            valid_attack = True







def main():
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")


if __name__ == '__main__':
    main()
