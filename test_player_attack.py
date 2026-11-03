from PlayerAttack import PlayerAttack, BOARD_SIZE, SHIP


# Create an empty test board
test_board = []

for row in range(BOARD_SIZE):
    new_row = []

    for column in range(BOARD_SIZE):
        new_row.append("~")

    test_board.append(new_row)


# Put one ship at row 2, column 3
test_board[2][3] = SHIP


# Create a PlayerAttack object
player = PlayerAttack()


# Test the attack system
player.attack(test_board)


# Show the results
print("Previous attacks:", player.previous_attacks)
print("Hits:", player.hits)
print("Misses:", player.misses)