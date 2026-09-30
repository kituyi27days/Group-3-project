
class Ship:
    # This section is responsible for the ship classes which would
    # called anytime we need to make a ship for a player. It will
    # also contain properties of the ship for functionality
    def __init__(self, name, size ):
        self.name = name
        self.size = size
        self.coordinates = [] # This will contain x and y cordinates of the gird
        self.orientation = "H" # By default orientation would be horizontal but can change to vertical
        self.hit = 0 # This can probably be done better but this is number of hits

    def is_sunk(self):
        return self.hits >= self.size # sink condition.
    
    # This section is repsoible for checking the board and ensuring ships are not
    # overlapping. I really need to understand how the code for person 1 works to implement this.
    # 
    def placement(board : list[list[str]], row : int, col : int, size : int, orientation : str):
        num_rows = len(board)
        num_cols = len(board[0])
        if orientation == "H":
            if (col + size) > num_cols:
                return "Collions with board"
            for c in range(col, col + size):
                if board[row][c] != "~":
                    return "Invalid Placement"
        elif orientation == "V":
            if (row + size) > num_rows:
                return "Collions with board"
            for c in range(row, row + size):
                if board[c][col] != "~":
                    return "Invalid Placement"
        else:
            return "Error with palcement"
        

    def is_valid():
        return 0
    def ship_placed():
        return 0
