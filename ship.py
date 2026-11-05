# =========================================================
# IMPORTS (From Person 1's board module & constants)
# =========================================================
from board import print_board, EMPTY, SHIP, BOARD_SIZE
import json
import random

HORIZONTAL = "H"
VERTICAL = "V"

def clear_screen():
    print("\033[2J\033[3J\033[H", end="", flush=True) 
# =========================================================
# SHIP CLASS (Person 2)
# =========================================================
class Ship:
    """
    Represents an individual ship in Battleship and manages its placement, 
    coordinates, and status on the 2D grid array.
    """
    def __init__(self, ship_name: str, size: int):
        self.ship_name = ship_name                  # Ship's name (e.g. "Carrier", "Battleship")
        self.size = size                            # Ship's length
        self.coordinates = []                       # List of occupied grid tuples: [(row, col), ...]
        self.orientation = HORIZONTAL               # "H" for Horizontal, "V" for Vertical
        self.hits = 0                               # Number of hits received

    def check_if_sunk(self) -> bool:
        """Returns True if the ship has taken hits equal to or exceeding its size."""
        return self.hits >= self.size

    def validate_placement(self, board: list[list[str]], row: int, col: int, orientation: str) -> bool:
        """
        Checks if the ship fits on the 10x10 board without going out of bounds 
        or overlapping existing ships ('~' represents untouched water).
        """
        num_rows = len(board)
        num_cols = len(board[0])
        orientation = orientation.upper()

        if orientation == HORIZONTAL:
            # 1. Right boundary check
            if col + self.size > num_cols:
                return False
            # 2. Overlap check against existing ships
            for c in range(col, col + self.size):
                if board[row][c] != EMPTY:
                    return False
                    
        elif orientation == VERTICAL:
            # 1. Bottom boundary check
            if row + self.size > num_rows:
                return False
            # 2. Overlap check against existing ships
            for r in range(row, row + self.size):
                if board[r][col] != EMPTY:
                    return False
        else:
            return False  # Invalid orientation input string

        return True

    def apply_placement(self, board: list[list[str]], row: int, col: int, orientation: str):
        """
        Updates the 2D grid cells with 'S' and stores the coordinates in self.coordinates.
        Must be called AFTER validate_placement() returns True.
        """
        self.orientation = orientation.upper()
        self.coordinates = []

        if self.orientation == HORIZONTAL:
            for c in range(col, col + self.size):
                board[row][c] = SHIP
                self.coordinates.append((row, c))
                
        elif self.orientation == VERTICAL:
            for r in range(row, row + self.size):
                board[r][col] = SHIP
                self.coordinates.append((r, col))


# =========================================================
# FLEET HELPER & SETUP LOOP
# =========================================================
def create_fleet() -> list[Ship]:
    """Instantiates the 5 standard Battleship game ships as objects."""
    return [
        Ship("Carrier", 5),
        Ship("Battleship", 4),
        Ship("Cruiser", 3),
        Ship("Submarine", 3),
        Ship("Destroyer", 2)
    ]



"""def setup_fleet(player_name: str, board: list[list[str]], fleet: list[Ship]):
    
    Interactively prompts the player to place all 5 ships in their fleet onto their 2D game board.
    
    print(f"\n==========================================")
    print(f" SHIP PLACEMENT PHASE: {player_name}")
    print(f"==========================================")
    
    for ship in fleet:
        placed = False
        while not placed:
            print_board(board, show_ships=True)
            print(f"\nPlacing: {ship.ship_name} (Size: {ship.size})")
            try:
                row = int(input(f"Enter starting ROW (0-{BOARD_SIZE - 1}): "))
                col = int(input(f"Enter starting COL (0-{BOARD_SIZE - 1}): "))
                orientation = input(f"Enter orientation ({HORIZONTAL} for Horizontal, {VERTICAL} for Vertical): ").strip().upper()

                # Validate input coordinates stay within 0-9 bounds
                if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                    print(f"⚠️ Invalid coordinates! Row and Column must be between 0 and {BOARD_SIZE - 1}.")
                    continue

                # Run validation logic via the Ship instance method
                if ship.validate_placement(board, row, col, orientation):
                    ship.apply_placement(board, row, col, orientation)
                    placed = True
                    print(f"✅ Successfully placed {ship.ship_name} at {ship.coordinates}!")
                else:
                    print("❌ Invalid placement! Ship goes out of bounds or overlaps another ship. Try again.")

            except ValueError:
                print("⚠️ Invalid input! Please enter integer numbers for Row and Column.")
                
    print(f"\n🎉 All ships successfully placed for {player_name}!\n")
    print_board(board)"""

def setup_computer_fleet(board, fleet):
    for ship in fleet:
        placed = False

        while not placed:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            orientation = random.choice([HORIZONTAL, VERTICAL])

            if ship.validate_placement(board, row, col, orientation):
                ship.apply_placement(board, row, col, orientation)
                placed = True

    print("Computer has placed all its ships!")

def setup_fleet(player_name: str, board: list[list[str]], fleet: list[Ship]):
    confirmations = []
    error_message = ""

    # Redraw one board and the successful placement messages.
    def show_placement():
        clear_screen()

        print(f"SHIP PLACEMENT: {player_name}\n")
        print_board(board, show_ships=True)

        for message in confirmations:
            print(message)

        if error_message:
            print(f"\n{error_message}")

    for ship in fleet:
        placed = False

        while not placed:
            show_placement()
            print(f"\nPlacing: {ship.ship_name} (Size: {ship.size})")

            try:
                row = int(
                    input(f"Enter starting ROW (0-{BOARD_SIZE - 1}): ")
                )
                col = int(
                    input(f"Enter starting COL (0-{BOARD_SIZE - 1}): ")
                )
                orientation = input(
                    f"Enter orientation ({HORIZONTAL} for Horizontal, "
                    f"{VERTICAL} for Vertical): "
                ).strip().upper()

                if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                    error_message = (
                        f"Row and Column must be between "
                        f"0 and {BOARD_SIZE - 1}."
                    )
                    continue

                if ship.validate_placement(board, row, col, orientation):
                    ship.apply_placement(board, row, col, orientation)

                    confirmations.append(
                        f"✅Successfully placed {ship.ship_name} "
                        f"at {ship.coordinates}!"
                    )

                    error_message = ""
                    placed = True
                else:
                    error_message = (
                        "❌Invalid placement! Check the orientation, "
                        "board boundaries, and overlapping ships."
                    )

            except ValueError:
                error_message = (
                    "Please enter integer numbers for Row and Column."
                )

    # Show the completed board with every ship visible.
    show_placement()
    print(f"\n🎉 All ships successfully placed for {player_name}!")

    input("Review your board, then press Enter to close it.")
    clear_screen()
    
def save_ships(player_ships, computer_ships, filename="savegame.json"):

    with open(filename, "r") as file:
        save_data = json.load(file)

    save_data["ships"] = {
        "player": [],
        "computer": []
    }

    for ship in player_ships:
        save_data["ships"]["player"].append({
            "name": ship.ship_name,
            "size": ship.size,
            "coordinates": ship.coordinates,
            "orientation": ship.orientation,
            "hits": ship.hits
        })

    for ship in computer_ships:
        save_data["ships"]["computer"].append({
            "name": ship.ship_name,
            "size": ship.size,
            "coordinates": ship.coordinates,
            "orientation": ship.orientation,
            "hits": ship.hits
        })

    with open(filename, "w") as file:
        json.dump(save_data, file, indent=4)

  