
# 1. Connect to board branch so that the computer can choose a row col to attack
import board

# computer generates random row col to attack
import random



#Create computer opponent

# repeat till gets a valid attack
#tracks the previous attacks using a list/dictionary decides whether it hit or missed
# and  uses functions to manage he computer turn
# the computer chooses a location to attack
# and checks if that location was attacked already


# FROM PLAYER-ATTACK BRANCH  -  to check which locations are already attacked
computer_previous_attacks = []


#CHECK IF COMPUTER ATTACK IS VALID
def already_attacked(attack_row, attack_col, previous_attacks):

    if[attack_row, attack_col] in previous_attacks:
        return True
    else:
        return False


#STORE COMPUTER ATTACKS
def record_attack(attack_row, attack_col, computer_previous_attacks):
    computer_previous_attacks.append([attack_row, attack_col])


#COPUTER ATTACK FUNCTION
def computer_attack(game_board, computer_previous_attacks):
    while True:
        attack_row = random.randint(0, board.BOARD_SIZE - 1)
        attack_col = random.randint(0, board.BOARD_SIZE - 1)

        if already_attacked(
            attack_row, attack_col, computer_previous_attacks
        ):
            continue

        record_attack(
            attack_row, attack_col, computer_previous_attacks
        )

        if game_board[attack_row][attack_col] == board.SHIP:
            game_board[attack_row][attack_col] = board.HIT
            return f"Hit at ({attack_row}, {attack_col})!"

        game_board[attack_row][attack_col] = board.MISS
        return f"Miss at ({attack_row}, {attack_col})."