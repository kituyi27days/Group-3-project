BOARD_SIZE = 10
SHIP = "S"
HIT = "X"
MISS = "O"

class PlayerAttack:
    def __init__(self):
        self.previous_attacks = []
        self.hits = 0
        self.misses = 0
    
    def get_attack_coordinates(self):
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

    def already_attacked(self, row, column):
        if [row, column] in self.previous_attacks:
            return True

        else:
            return False
    
    def record_attack(self, row, column):
        self.previous_attacks.append([row, column])
    
    def attack(self, board):
        valid_attack = False

        while valid_attack == False:
            attack_row, attack_column = self.get_attack_coordinates()

            if self.already_attacked(attack_row, attack_column):
                print("You already attacked this location. Choose another location.")

            else:
                self.record_attack(attack_row, attack_column)

                if board[attack_row][attack_column] == SHIP:
                    board[attack_row][attack_column] = HIT
                    self.hits += 1
                    print("Hit!")

                else:
                    board[attack_row][attack_column] = MISS
                    self.misses += 1
                    print("Miss!")

                valid_attack = True
    
    def to_dict(self):
        data = {
            "previous_attacks": self.previous_attacks,
            "hits": self.hits,
            "misses": self.misses
        }

        return data
    
    def from_dict(self):
        self.previous_attacks = data["previous_attacks"]
        self.hits = data["hits"]
        self.misses = data["misses"]

        


