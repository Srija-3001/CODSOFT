import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

board = [""] * 9
buttons = []

# Check winner
def check_winner(brd):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win_combinations:
        if brd[a] == brd[b] == brd[c] and brd[a] != "":
            return brd[a]

    if "" not in brd:
        return "Draw"

    return None

# Minimax Algorithm
def minimax(brd, is_maximizing):
    result = check_winner(brd)

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(9):
            if brd[i] == "":
                brd[i] = "O"
                score = minimax(brd, False)
                brd[i] = ""
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = 100
        for i in range(9):
            if brd[i] == "":
                brd[i] = "X"
                score = minimax(brd, True)
                brd[i] = ""
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    buttons[move].config(text="O", state="disabled")

    result = check_winner(board)

    if result:
        end_game(result)

# Player Move
def player_move(index):
    if board[index] == "":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        result = check_winner(board)

        if result:
            end_game(result)
            return

        ai_move()

# End Game
def end_game(result):
    if result == "Draw":
        messagebox.showinfo("Game Over", "It's a Draw!")
    else:
        messagebox.showinfo("Game Over", f"{result} Wins!")

    reset_game()

# Reset Board
def reset_game():
    global board

    board = [""] * 9

    for button in buttons:
        button.config(text="", state="normal")

# Create Buttons
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        width=8,
        height=3,
        font=("Arial", 20),
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Restart Button
restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)

restart_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()