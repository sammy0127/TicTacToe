"""
Tic Tac Toe Game in Python Using Tkinter

requires tkinter version 8.6 or greater
"""
import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__(self)
        self.title("Tic Tac Toe!")
        self._cells = {}
        # self._create_board_display(self)

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )


def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == "__main__":
    main()
