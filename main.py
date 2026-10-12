# =========================================================
# PERSON 5: GAME ORCHESTRATION & TURN SYSTEM (main.py)
# =========================================================

import random
from board import create_board, print_board, BOARD_SIZE, SHIP, HIT, MISS, EMPTY
from ship import create_fleet, setup_fleet

def check_game_over(fleet: list) -> bool:
    """Returns True if every ship in the fleet is sunk."""
    return all(ship.check_if_sunk() for ship in fleet)

def ai_setup_fleet(board: list[list[str]], fleet: list):
    """
    Randomly places the computer's fleet on its board 
    without overlapping or going out of bounds.
    """
    for ship in fleet:
        placed = False
        while not placed:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            orientation = random.choice(["H", "V"])
            
            if ship.validate_placement(board, row, col, orientation):
                ship.apply_placement(board, row, col, orientation)
                placed = True

def main():
    print("==========================================")
    print("      WELCOME TO PYTHON BATTLESHIP        ")
    print("==========================================")

    # 1. Initialize Boards & Fleets for Player and Computer
    player_board = create_board()
    computer_board = create_board()

    player_fleet = create_fleet()
    computer_fleet = create_fleet()

    # 2. Setup Phase
    print("\n--- PLAYER FLEET SETUP ---")
    setup_fleet("Human Player", player_board, player_fleet)

    print("\n--- COMPUTER FLEET SETUP ---")
    ai_setup_fleet(computer_board, computer_fleet)
    print(" AI has successfully placed its hidden fleet!")

    # Track already attacked coordinates to prevent duplicate shots
    player_attacks = set()
    ai_attacks = set()

    # 3. Main Battle Loop
    game_over = False
    turn = 1

    while not game_over:
        print(f"\n=================== TURN {turn} ===================")
        print("\n--- ENEMY BOARD (TARGETS) ---")
        print_board(computer_board, show_ships=False)

        print("\n--- YOUR BOARD ---")
        print_board(player_board, show_ships=True)

        # =========================================================
        # PLAYER TURN
        # =========================================================
        valid_shot = False
        while not valid_shot:
            try:
                row = int(input("\nEnter target ROW (0-9): "))
                col = int(input("Enter target COL (0-9): "))

                if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                    print(f"Target out of bounds! Choose coordinates between 0 and {BOARD_SIZE - 1}.")
                    continue

                target_coord = (row, col)
                if target_coord in player_attacks:
                    print("You already shot at those coordinates! Pick another spot.")
                    continue

                player_attacks.add(target_coord)
                cell = computer_board[row][col]

                if cell == SHIP:
                    computer_board[row][col] = HIT
                    print("BOOM! Direct Hit on an enemy ship!")
                    for ship in computer_fleet:
                        if target_coord in ship.coordinates:
                            ship.hits += 1
                            if ship.check_if_sunk():
                                print(f"DESTROYED! You completely sunk the enemy's {ship.ship_name}!")
                            break
                    valid_shot = True
                else:
                    computer_board[row][col] = MISS
                    print("Splash! Missed—open water.")
                    valid_shot = True

            except ValueError:
                print("Please enter valid integers for Row and Column.")

        # Check if Player won
        if check_game_over(computer_fleet):
            print("\n CONGRATULATIONS! You sunk all enemy ships and won the game!")
            print_board(computer_board, show_ships=True)
            break

        # =========================================================
        # COMPUTER TURN
        # =========================================================
        print("\n--- COMPUTER'S TURN ---")
        comp_valid = False
        while not comp_valid:
            c_row = random.randint(0, BOARD_SIZE - 1)
            c_col = random.randint(0, BOARD_SIZE - 1)
            comp_coord = (c_row, c_col)

            if comp_coord not in ai_attacks:
                ai_attacks.add(comp_coord)
                c_cell = player_board[c_row][c_col]

                if c_cell == SHIP:
                    player_board[c_row][c_col] = HIT
                    print(f"Computer struck your ship at Row {c_row}, Col {c_col}!")
                    for ship in player_fleet:
                        if comp_coord in ship.coordinates:
                            ship.hits += 1
                            if ship.check_if_sunk():
                                print(f"🔥 Oh no! The computer completely destroyed your {ship.ship_name}!")
                            break
                else:
                    player_board[c_row][c_col] = MISS
                    print(f" Computer attacked Row {c_row}, Col {c_col} and missed.")
                comp_valid = True

        # Check if Computer won
        if check_game_over(player_fleet):
            print("\n GAME OVER! The computer sunk all your ships!")
            print_board(player_board, show_ships=True)
            break

        turn += 1

if __name__ == "__main__":
    main()