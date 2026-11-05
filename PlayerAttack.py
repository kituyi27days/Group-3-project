from board import SHIP, HIT, MISS, BOARD_SIZE
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--show-history",
    action="store_true",
    help="Show the player's previous attack coordinates"
)

args = parser.parse_args()





class PlayerAttack:

    def __init__(self, show_history=False):
        self.previous_attacks = []
        self.hits = 0
        self.misses = 0
        self.show_history = show_history 


    def get_attack_coordinates(self):

        valid_coordinates = False

        while valid_coordinates == False:

            try:
                attack_row = int(
                    input("Enter the row you want to attack between 0 and 9 (inclusive): ")
                )

                attack_column = int(
                    input("Enter the column you want to attack between 0 and 9 (inclusive): ")
                )

                if attack_row < 0 or attack_row >= BOARD_SIZE:
                    print("Invalid row. Please enter a value between 0 and 9.")

                elif attack_column < 0 or attack_column >= BOARD_SIZE:
                    print("Invalid column. Please enter a value between 0 and 9.")

                else:
                    valid_coordinates = True

            except ValueError:
                print("Please enter numbers only.")

        return attack_row, attack_column


    def already_attacked(self, row, column):

        if [row, column] in self.previous_attacks:
            return True

        else:
            return False


    def record_attack(self, row, column):

        self.previous_attacks.append([row, column])


    def attack(self, board):

        attack_row, attack_column = self.get_attack_coordinates()

        if self.already_attacked(attack_row, attack_column):
            print("You already attacked this location. Choose another location.")
            return self.attack(board)

        self.record_attack(attack_row, attack_column)

        if board[attack_row][attack_column] == SHIP:
            board[attack_row][attack_column] = HIT
            self.hits += 1
            return f"Hit at ({attack_row}, {attack_column})!"
        else:
            board[attack_row][attack_column] = MISS
            self.misses += 1
            return f"Miss at ({attack_row}, {attack_column})."


    def attack_at(self, board, attack_row, attack_column):

        if attack_row < 0 or attack_row >= BOARD_SIZE:
            return "Invalid row"

        if attack_column < 0 or attack_column >= BOARD_SIZE:
            return "Invalid column"

        if self.already_attacked(attack_row, attack_column):
            return "Already attacked"

        self.record_attack(attack_row, attack_column)

        if board[attack_row][attack_column] == SHIP:
            board[attack_row][attack_column] = HIT
            self.hits += 1
            return "Hit!"

        else:
            board[attack_row][attack_column] = MISS
            self.misses += 1
            return "Miss!"
    

    def to_dict(self):

        data = {
            "previous_attacks": self.previous_attacks,
            "hits": self.hits,
            "misses": self.misses
        }

        return data


    def from_dict(self, data):

        self.previous_attacks = data["previous_attacks"]
        self.hits = data["hits"]
        self.misses = data["misses"]


    def save_state(self, filename="savegame.json"):

        try:
            with open(filename, "r") as file:
                save_data = json.load(file)

        except FileNotFoundError:
            save_data = {
                "board": {},
                "ships": {},
                "player_attack": {},
                "computer": {},
                "game_state": {}
            }

        except json.JSONDecodeError:
            save_data = {
                "board": {},
                "ships": {},
                "player_attack": {},
                "computer": {},
                "game_state": {}
            }

        save_data["player_attack"] = self.to_dict()

        with open(filename, "w") as file:
            json.dump(save_data, file, indent=4)


    def load_state(self, filename="savegame.json"):

        try:
            with open(filename, "r") as file:
                save_data = json.load(file)

            if "player_attack" in save_data:

                player_attack_data = save_data["player_attack"]

                if player_attack_data != {}:
                    self.from_dict(player_attack_data)

        except FileNotFoundError:
            print("No saved game was found.")

        except json.JSONDecodeError:
            print("The save file is empty or invalid.")

    





    


        


