import argparse

# --- CONSTANTS ---
DEFAULT_BOARD_SIZE = 10
EMPTY = "~"
SHIP = "S"
HIT = "X"
MISS = "O"


# --- RECURSION REQUIREMENT (Person 1) ---
def create_board_recursive(size=DEFAULT_BOARD_SIZE, current_row=0):
    """
    Recursively constructs a 2D grid of size x size initialized with '~' cells.
    Base case: stops when current_row reaches size.
    """
    if current_row >= size:
        return []
    
    row = [EMPTY] * size
    return [row] + create_board_recursive(size, current_row + 1)


# --- BOARD DISPLAY FUNCTION ---
def print_board(board, show_ships=False):
    """
    Prints the 2D grid formatted with column numbers and row indices.
    Hides ships ('S') as '~' unless show_ships is True.
    """
    size = len(board)
    print("   " + " ".join(str(i) for i in range(size)))
    print("  " + "-" * (size * 2 + 1))

    for row_number, row in enumerate(board):
        display_row = []
        for cell in row:
            if cell == SHIP and not show_ships:
                display_row.append(EMPTY)
            else:
                display_row.append(cell)
        
        row_string = " ".join(display_row)
        print(f"{row_number} | {row_string}")


# --- ARGPARSE REQUIREMENT (Person 1) ---
def parse_arguments():
    """
    Parses command-line arguments to customize game parameters.
    """
    parser = argparse.ArgumentParser(
        description="CSCI 1030U Battleship - Group 3 Board Logic"
    )
    parser.add_argument(
        "--size", 
        type=int, 
        default=DEFAULT_BOARD_SIZE, 
        help="Grid size for the board (default: 10)"
    )
    parser.add_argument(
        "--reveal-ships", 
        action="store_true", 
        help="Debug flag to display hidden ship locations"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    game_board = create_board_recursive(args.size)
    print_board(game_board, show_ships=args.reveal_ships)