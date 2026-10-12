
BOARD_SIZE = 10
EMPTY = "~"
SHIP = "S"
HIT = "X"
MISS = "O"
HORIZONTAL = "H"
VERTICAL = "V"
PLAYER = "Player"
COMPUTER = "Computer"
TOTAL_SHIPS = 5
 
def create_board(size=BOARD_SIZE) -> list:
    """Creates a fresh 10x10 board filled with '~' using simple loops."""
    board = []# Initialize locally so it resets each time
    for r in range(size):
        row = []
        for c in range(size):
            row.append(EMPTY)
        board.append(row)
    return board

def print_board(board, show_ships=False):
    """Prints the board cleanly with row and column numbers."""
    print("    0 1 2 3 4 5 6 7 8 9")
    print("  ---------------------")

    row_number = 0
    for row in board:
        display_row = []
        for cell in row:
            # Hide ships from enemy view if show_ships is False
            if cell == SHIP and not show_ships:
                display_row.append(EMPTY)
            else:
                display_row.append(cell)
        
        # Combine the list into a single line string separated by spaces
        row_string = " ".join(display_row)
        print(f"{row_number} | {row_string}")
        row_number += 1