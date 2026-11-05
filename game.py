from board import create_board, print_board, SHIP, HIT
from Computer import ComputerOpponent
from PlayerAttack import PlayerAttack
from ship import create_fleet, setup_fleet, setup_computer_fleet, clear_screen


player : str = "Player"
computer : str = "Computer"

game_state = {
    "turn" : player,
    "winner" : None,
    "game_over" : False,

}

# call the function that has all the ships and let the player place them, we already have the function that checks wether a postion is allowed or not so if it is allowed i'll call the function and make the player select their position for their ships


def switch_turn():
    if game_state["turn"] == player:
        game_state["turn"] = computer
    else:
        game_state["turn"] = player


def check_winner(player_board, computer_board):
    player_has_ships = False
    computer_has_ships = False

    for row in player_board:
        if SHIP in row:
            player_has_ships = True

    for row in computer_board:
        if SHIP in row:
            computer_has_ships = True

    if not player_has_ships:
        return computer

    if not computer_has_ships:
        return player

    return None


def choose_game_mode():
    print("Choose game mode:")
    print("1. Play against computer")
    print("2. Play against another player")

    choice = input("Enter 1 or 2: ")

    while choice != "1" and choice != "2":
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter 1 or 2: ")

    if choice == "1":
        return "Computer"
    else:
        return "Player"

def run_game():
    

    game_mode = choose_game_mode()

    player_board = create_board()
    computer_board = create_board()
    

    if game_mode == "Player":
        # Create separate ships for each player.
        player_ships = create_fleet()
        second_player_ships = create_fleet()

        print("\nPlayer 2, look away while Player 1 places their ships.")
        input("Player 1, press Enter when ready.")

        setup_fleet("Player 1", player_board, player_ships)

        print("\nPlayer 1, look away while Player 2 places their ships.")
        input("Player 2, press Enter when ready.")

        setup_fleet("Player 2", computer_board, second_player_ships)
    else:
        player_ships = create_fleet()
        computer_ships = create_fleet()
        computer_opponent = ComputerOpponent()

        setup_fleet("Player", player_board, player_ships)
        setup_computer_fleet(computer_board, computer_ships)




    player_attacker = PlayerAttack()
    second_player_attacker = PlayerAttack()

    

    player_result = ""
    opponent_result = ""

    opponent_name = "Computer"
    if game_mode == "Player":
        opponent_name = "Player 2"

    while not game_state["game_over"]:
        show_battle_boards(player_board, computer_board, game_mode)

        # Keep only the latest result for each side.
        if player_result:
            print(f"\nPlayer 1: {player_result}")
        if opponent_result:
            print(f"{opponent_name}: {opponent_result}")

        if game_state["turn"] == player:
            print("\nPlayer 1's turn — attack the opponent's board.")
            player_result = player_attacker.attack(computer_board)
        elif game_mode == "Computer":
            # The opponent keeps its own attack history and statistics.
            attack_coordinates = computer_opponent.computer_attack(player_board)

            if attack_coordinates is None:
                opponent_result = "All positions have already been attacked."
            else:
                row, col = attack_coordinates
                if player_board[row][col] == HIT:
                    opponent_result = f"Hit at ({row}, {col})!"
                else:
                    opponent_result = f"Miss at ({row}, {col})."
        else:
            print("\nPlayer 2's turn — attack Player 1's board.")
            opponent_result = second_player_attacker.attack(player_board)

        game_state["winner"] = check_winner(player_board, computer_board)

        if game_state["winner"] is not None:
            game_state["game_over"] = True
        else:
            switch_turn()

    # Show the final attack before announcing the winner.
    show_battle_boards(player_board, computer_board, game_mode)
    if player_result:
        print(f"\nPlayer 1: {player_result}")
    if opponent_result:
        print(f"{opponent_name}: {opponent_result}")

    winner_name = "Player 1"
    if game_state["winner"] == computer:
        winner_name = opponent_name
    print(f"\n{winner_name} wins!")


def show_battle_boards(player_board, computer_board, game_mode):
    clear_screen()

    opponent_name = "Computer"
    if game_mode == "Player":
        opponent_name = "Player 2"

    print("X = hit | O = miss | ~ = unknown\n")

    print("Player 1's board — attacks received:")
    print_board(player_board, show_ships=False)

    print(f"\n{opponent_name}'s board — attacks received:")
    print_board(computer_board, show_ships=False)

if __name__ == "__main__":
    
    run_game()


# while game isn't over:

#     Is it player's turn?
#         ↓
#     Player attacks
#         ↓
#     Check winner
#         ↓
#     If nobody won:
#         switch turn

#     Computer's turn
#         ↓
#     Computer attacks
#         ↓
#     Check winner
#         ↓
#     If nobody won:
#         switch turn