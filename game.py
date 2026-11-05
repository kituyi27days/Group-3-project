
import json

from board import save_board_state, create_board, print_board, SHIP, HIT
from Computer import ComputerOpponent
from PlayerAttack import PlayerAttack
from ship import (
    save_ships,
    load_ships,
    create_fleet,
    setup_fleet,
    setup_computer_fleet,
    clear_screen
)


player = "Player"
computer = "Computer"


# =========================================================
# GAME CONTROLLER
# =========================================================

class GameController:

    def __init__(self):
        self.turn = player
        self.winner = None
        self.game_over = False

    def switch_turn(self):
        if self.turn == player:
            self.turn = computer
        else:
            self.turn = player

    def check_winner(self, player_board, computer_board):

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


# =========================================================
# SAVE AND LOAD GAME STATE
# =========================================================

def save_game_state(controller, game_mode, filename="savegame.json"):

    try:
        with open(filename, "r") as file:
            save_data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        save_data = {}

    save_data["game_state"] = {
        "turn": controller.turn,
        "winner": controller.winner,
        "game_over": controller.game_over,
        "game_mode": game_mode
    }

    with open(filename, "w") as file:
        json.dump(save_data, file, indent=4)


def load_game_state(filename="savegame.json"):

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return None


# =========================================================
# CHOOSE GAME MODE
# =========================================================

def choose_game_mode():

    print("Choose game mode:")
    print("1. Play against computer")
    print("2. Play against another player")

    choice = input("Enter 1 or 2: ")

    while choice not in ("1", "2"):
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter 1 or 2: ")

    if choice == "1":
        return "Computer"

    return "Player"


# =========================================================
# RUN GAME
# =========================================================

def run_game():

    controller = GameController()

    saved_data = load_game_state()
    continue_saved_game = False

    # -----------------------------------------------------
    # CHECK FOR A PREVIOUSLY SAVED GAME
    # -----------------------------------------------------

    if (
        saved_data is not None
        and saved_data.get("game_state", {}).get("game_mode") == "Computer"
    ):

        print("1. Continue saved game")
        print("2. Start a new game")

        choice = input("Choose 1 or 2: ")

        while choice not in ("1", "2"):
            choice = input("Invalid choice. Enter 1 or 2: ")

        if choice == "1":

            try:
                player_board = saved_data["board"]["player"]["grid"]
                computer_board = saved_data["board"]["computer"]["grid"]

                controller.turn = saved_data["game_state"]["turn"]
                controller.winner = saved_data["game_state"]["winner"]
                controller.game_over = saved_data["game_state"]["game_over"]

                continue_saved_game = True
                game_mode = "Computer"

            except (KeyError, TypeError):
                print("The saved game is incomplete. Starting a new game.")

                game_mode = choose_game_mode()
                player_board = create_board()
                computer_board = create_board()

        else:
            game_mode = choose_game_mode()
            player_board = create_board()
            computer_board = create_board()

    else:
        game_mode = choose_game_mode()
        player_board = create_board()
        computer_board = create_board()

    # -----------------------------------------------------
    # SET UP SHIPS AND COMPUTER
    # -----------------------------------------------------

    if game_mode == "Player":

        player_ships = create_fleet()
        second_player_ships = create_fleet()

        print("\nPlayer 2, look away while Player 1 places their ships.")
        input("Player 1, press Enter when ready.")

        setup_fleet("Player 1", player_board, player_ships)

        print("\nPlayer 1, look away while Player 2 places their ships.")
        input("Player 2, press Enter when ready.")

        setup_fleet("Player 2", computer_board, second_player_ships)

    else:

        computer_opponent = ComputerOpponent()

        if continue_saved_game:

            computer_opponent.load_data()
            player_ships, computer_ships = load_ships()

        else:

            player_ships = create_fleet()
            computer_ships = create_fleet()

            setup_fleet("Player", player_board, player_ships)
            setup_computer_fleet(computer_board, computer_ships)

            save_ships(player_ships, computer_ships)

    # -----------------------------------------------------
    # SET UP ATTACKERS
    # -----------------------------------------------------

    player_attacker = PlayerAttack()
    second_player_attacker = PlayerAttack()

    if continue_saved_game:
        player_attacker.load_state()

    player_result = ""
    opponent_result = ""

    opponent_name = "Computer"

    if game_mode == "Player":
        opponent_name = "Player 2"

    # Save the initial game state for a new game.
    if not continue_saved_game:
        save_board_state(player_board, computer_board)
        save_game_state(controller, game_mode)

    # -----------------------------------------------------
    # MAIN GAME LOOP
    # -----------------------------------------------------

    while not controller.game_over:

        show_battle_boards(player_board, computer_board, game_mode)

        if player_result:
            print(f"\nPlayer 1: {player_result}")

        if opponent_result:
            print(f"{opponent_name}: {opponent_result}")

        # PLAYER'S TURN
        if controller.turn == player:

            print("\nPlayer 1's turn — attack the opponent's board.")

            player_result = player_attacker.attack(computer_board)

            player_attacker.save_state()

        # COMPUTER'S TURN
        elif game_mode == "Computer":

            attack_coordinates = computer_opponent.computer_attack(player_board)

            if attack_coordinates is None:

                opponent_result = "All positions have already been attacked."

            else:

                row, col = attack_coordinates

                if player_board[row][col] == HIT:
                    opponent_result = f"Hit at ({row}, {col})!"

                else:
                    opponent_result = f"Miss at ({row}, {col})."

            computer_opponent.save_data()

        # PLAYER 2'S TURN
        else:

            print("\nPlayer 2's turn — attack Player 1's board.")

            opponent_result = second_player_attacker.attack(player_board)

        # SAVE BOARDS
        save_board_state(player_board, computer_board)

        # CHECK FOR WINNER
        controller.winner = controller.check_winner(
            player_board,
            computer_board
        )

        if controller.winner is not None:
            controller.game_over = True

        else:
            controller.switch_turn()

        # SAVE UPDATED GAME STATE
        save_game_state(controller, game_mode)

    # -----------------------------------------------------
    # ANNOUNCE WINNER
    # -----------------------------------------------------

    show_battle_boards(player_board, computer_board, game_mode)

    if player_result:
        print(f"\nPlayer 1: {player_result}")

    if opponent_result:
        print(f"{opponent_name}: {opponent_result}")

    winner_name = "Player 1"

    if controller.winner == computer:
        winner_name = opponent_name

    print(f"\n{winner_name} wins!")


# =========================================================
# DISPLAY BOARDS
# =========================================================

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


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    run_game()
