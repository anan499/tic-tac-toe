import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        master.configure(bg='lightblue')  # Set the background color of the window
        master.geometry("400x400")  # Set the window size (width x height)

        self.board = [" " for _ in range(9)]  # Board initialization
        self.current_player = "X"
        self.buttons = []

        # Create the 3x3 grid of buttons
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", font=("Arial", 24), width=5, height=2, bg='white',
                                   activebackground='lightgray', fg='blue', bd=5, relief='raised', 
                                   highlightbackground='gray', highlightcolor='red', 
                                   command=lambda idx=i*3+j: self.make_move(idx))
                button.grid(row=i, column=j, sticky='nsew')
                row.append(button)
            self.buttons.append(row)

        # Configure grid weights to center the buttons
        for i in range(3):
            master.grid_rowconfigure(i, weight=1)  # Allow rows to expand
            master.grid_columnconfigure(i, weight=1)  # Allow columns to expand

    def make_move(self, idx):
        if self.board[idx] == " ":
            self.board[idx] = self.current_player
            if self.current_player == "X":
                self.buttons[idx // 3][idx % 3].config(text=self.current_player, fg='red')  # Set text color to red for "X"
            else:
                self.buttons[idx // 3][idx % 3].config(text=self.current_player, fg='blue')  # Set text color to blue for "O"

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.config(text=" ", fg='blue')  # Reset text color for new game

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
