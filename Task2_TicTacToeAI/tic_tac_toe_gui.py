import tkinter as tk
from tkinter import messagebox

board = [""] * 9

def check_winner():
    winning_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None

def ai_move():
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            buttons[i].config(text="O", state="disabled")
            break

    result = check_winner()

    if result:
        end_game(result)

def player_move(index):
    if board[index] == "":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        result = check_winner()

        if result:
            end_game(result)
            return

        ai_move()

def end_game(result):
    if result == "Draw":
        messagebox.showinfo("Game Over", "It's a Draw!")
    else:
        messagebox.showinfo("Game Over", f"{result} Wins!")

    root.destroy()

root = tk.Tk()
root.title("Tic-Tac-Toe AI")

buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        width=10,
        height=4,
        font=("Arial", 18),
        command=lambda i=i: player_move(i)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()