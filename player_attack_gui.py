import tkinter as tk
from PlayerAttack import PlayerAttack, BOARD_SIZE, SHIP



# Temporary board for testing


board = []

for row in range(BOARD_SIZE):
    new_row = []

    for column in range(BOARD_SIZE):
        new_row.append("~")

    board.append(new_row)

# Temporary ships for testing
board[2][3] = SHIP
board[5][6] = SHIP


player_attack = PlayerAttack()


# Button function


def attack_button_clicked():
    try:
        attack_row = int(row_entry.get())
        attack_column = int(column_entry.get())

        result = player_attack.attack_at(
            board,
            attack_row,
            attack_column
        )

        result_label.config(text=result)

        stats_label.config(
            text="Hits: "
            + str(player_attack.hits)
            + " | Misses: "
            + str(player_attack.misses)
        )

        history_label.config(
            text="Previous attacks: "
            + str(player_attack.previous_attacks)
        )

        row_entry.delete(0, tk.END)
        column_entry.delete(0, tk.END)

    except ValueError:
        result_label.config(text="Please enter numbers only.")



# Window


window = tk.Tk()

window.title("Battleship - Player Attack")
window.geometry("450x450")

# Light background
window.configure(bg="white")


# Title
title_label = tk.Label(
    window,
    text="Player Attack",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="black"
)

title_label.pack(pady=20)



# Row

row_label = tk.Label(
    window,
    text="Row (0-9):",
    font=("Arial", 14),
    bg="white",
    fg="black"
)

row_label.pack()

row_entry = tk.Entry(
    window,
    width=15,
    font=("Arial", 14),
    bg="white",
    fg="black"
)

row_entry.pack(pady=8)



# Column
column_label = tk.Label(
    window,
    text="Column (0-9):",
    font=("Arial", 14),
    bg="white",
    fg="black"
)

column_label.pack()

column_entry = tk.Entry(
    window,
    width=15,
    font=("Arial", 14),
    bg="white",
    fg="black"
)

column_entry.pack(pady=8)



# Attack Button
attack_button = tk.Button(
    window,
    text="Attack",
    font=("Arial", 14, "bold"),
    command=attack_button_clicked
)

attack_button.pack(pady=20)


# Result
result_label = tk.Label(
    window,
    text="Choose a location to attack.",
    font=("Arial", 14),
    bg="white",
    fg="black"
)

result_label.pack(pady=8)


# Stats
stats_label = tk.Label(
    window,
    text="Hits: 0 | Misses: 0",
    font=("Arial", 13),
    bg="white",
    fg="black"
)

stats_label.pack(pady=8)


# History

history_label = tk.Label(
    window,
    text="Previous attacks: []",
    font=("Arial", 12),
    bg="white",
    fg="black",
    wraplength=400
)

history_label.pack(pady=8)


window.mainloop()