
# 1. Connect to board branch so that the computer can choose a row col to attack
import board
# computer generates random row col to attack
import random
import json


class ComputerOpponent:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.computer_previous_attacks = [] # stores locations alr attacked
        self.hits = 0
        self.misses = 0
#Create computer opponent

# repeat till gets a valid attack
#tracks the previous attacks using a list/dictionary decides whether it hit or missed
# and  uses functions to manage he computer turn
# the computer chooses a location to attack
# and checks if that location was attacked already


# FROM PLAYER-ATTACK BRANCH  -  to check which locations are already attacked
#computer_previous_attacks = []


#CHECK IF COMPUTER ATTACK IS VALID-> ATTACKED
    def already_attacked(self,attack_row, attack_col): # def already_attacked(attack_row, attack_col, previous_attacks):


        if [attack_row, attack_col] in self.computer_previous_attacks: #if[attack_row, attack_col] in previous_attacks:
            return True
        else:
            return False


#STORE COMPUTER ATTACKS
    def record_attack(self,attack_row, attack_col):
        self.computer_previous_attacks.append([attack_row, attack_col])

    #STORE COMPUTER ATTACKS
    # def record_attack(attack_row, attack_col, computer_previous_attacks):
    #     computer_previous_attacks.append([attack_row, attack_col])


#COMPUTER ATTACK FUNCTION
    def computer_attack(self, game_board): #def computer_attack(game_board, computer_previous_attacks):

        if self.all_positions_attacked(game_board):  # recursion function 
            print("Computer attacked at every position!")
            return None # all positions are taken

        valid_attack = False
        
        while valid_attack == False:

            # board size comes form borad.py
            # #randint includes 0-9 size of board

            attack_row = random.randint(0, len(game_board) - 1)
            #attack_row = random.randint(0, board.BOARD_SIZE - 1)

            attack_col = random.randint(0, len(game_board[attack_row]) - 1)


# check if the random genrated location is attacked already
            if self.already_attacked(attack_row, attack_col):
                #  if already_attacked(attack_row, attack_col,computer_previous_attacks):
                print("Computer already attacked this location. Generating a new attack...")
            
            else:
                #store the attack in th list
                self.record_attack(attack_row, attack_col)


                # refer to board class - check if the attack was a hit or miss
                if game_board[attack_row][attack_col] == board.SHIP:
                    game_board[attack_row][attack_col] = board.HIT
                    self.hits+=1
                    print("Computer hit a ship!")
 
                else:
                    #no ship at the location
                    game_board[attack_row][attack_col] = board.MISS
                    self.misses+=1
                    print("Computer missed")

        
                # successful at making an attack so end loop 
                valid_attack = True

        return attack_row, attack_col
    # SAVE FILE I/O --> reading/writing to json file 
    def save_data(self): # creats dictionary with the data
        data = {"difficulty": self.difficulty, "hits": self.hits ,"misses":self.misses ,"attacks": self.computer_previous_attacks}

        with open("computer_s.json","w") as file:
            json.dump(data, file, indent = 4) #writes data into the file
    def load_data(self): # LOADS DATA INTO FILE 
        try:
            with open("computer_s.json", "r") as file:
                data = json.load(file) #load reads the saved data dictionary and restores
                self.difficulty = data["difficulty"]
                self.hits = data["hits"]
                self.misses = data["misses"]
                self.computer_previous_attacks = data["attacks"]
        except FileNotFoundError:
            print("File does not exist")

    def all_positions_attacked(self, game_board, position=0): # check if attacked every position on board
        total_positions = len(game_board) * len(game_board[0]) #10*10

        # BASE CASE
        if position  == total_positions: 
            return True

        columns  = len(game_board[0]) # to figure out row and col of position num
        row = position // columns
        col = position % columns

        # now check if its attacked or not 

        if not self.already_attacked(row,col):
            return False

        #RECURSIVE : moves on to next positon to check 
        return self.all_positions_attacked(game_board, position +1)

        


#test save load #from Computer import ComputerOpponent

# c = ComputerOpponent()

# c.hits = 3
# c.misses = 2
# c.computer_previous_attacks = [[0, 1], [1, 2]]

# c.save_data()

# d = ComputerOpponent()
# d.load_data()

# print(d.difficulty, d.hits, d.misses, d.computer_previous_attacks)

# python -c "from Computer import ComputerOpponent; c = ComputerOpponent(); b = [['~','~'],['~','~']]; print(c.all_positions_attacked(b)); c.computer_previous_attacks = [[0,0],[0,1],[1,0],[1,1]]; print(c.all_positions_attacked(b))"




        