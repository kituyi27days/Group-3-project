player : str = "Player"
computer : str = "Computer"

game_state = {
    "turn" : player,
    "winner" : None,
    "game_over" : False

}

# call the function that has all the ships and let the player place them, we already have the function that checks wether a postion is allowed or not so if it is allowed i'll call the function and make the player select their position for their ships


def switch_turn():
    if game_state["turn"] == player:
        game_state["turn"] = computer
    else:
        game_state["turn"] = player


def check_winner(player_ships, computer_ships): # players_ship, computer_ships is how many ships are remaning ////TEMPO////
    if len(player_ships) == 0:
        return computer
    if len(computer_ships) == 0:
        return player

    return None 

def run_game():
    while game_state["game_over"] == False:
            if game_state["turn"] == player:
                print("Player's turn") #put player attack function here or call it

            else: 
                print("Computers turn") #put computer function here or call it

            switch_turn()



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