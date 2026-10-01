from board import create_board, print_board
from Computer import computer_attack
from PlayerAttack import player_attack


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


def check_winner(player_ships, computer_ships): # players_ship, computer_ships is how many ships are remaning ////TEMPO////
    if len(player_ships) == 0:
        return computer      # a ship can be hit/sunk without neccesarily being removed from player's or computer's ship list so need to look at person 2 code
    if len(computer_ships) == 0:
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

    computer_previous_attacks = []
    player_previous_attacks = []

    print("Player board:")
    print_board(player_board, show_ships=True)

    print("Computer board:")
    print_board(computer_board)


    while game_state["game_over"] == False:

        if game_state["turn"] == player:
            print("Player's turn")
            player_attack(computer_board, player_previous_attacks)
            # call Person 3's attack function here

        else:
        
            if game_mode == "Computer":
                print("Computers turn")
                computer_attack(player_board, computer_previous_attacks)

        # call Person 4's attack function here

            else:
                print("Player 2's turn")

        # call the player 2 attack function here

            # call Person 4's attack function here

        # check if someone won

        if game_state["winner"] != None:
            game_state["game_over"] = True
        else:
            switch_turn()

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