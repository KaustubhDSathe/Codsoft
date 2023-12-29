import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        return "It's a tie! You both chose {}".format(user_choice)
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return "You win! {} beats {}".format(user_choice, computer_choice)
    else:
        return "You lose! {} beats {}".format(computer_choice, user_choice)

def play_game(user_choice):
    result = determine_winner(user_choice)
    messagebox.showinfo("Result", result)

def create_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    instruction_label = tk.Label(
        root, text="Select Rock, Paper, or Scissors:", font=("Helvetica", 12)
    )
    instruction_label = tk.Label(
        root, text="Winning rules of the game ROCK PAPER SCISSORS are :\n+ Rock vs Paper -> Paper wins \n+ Rock vs Scissors -> Rock wins \n+ Paper vs Scissors -> Scissor wins \n", font=("Helvetica", 12)
    )
    instruction_label.pack(pady=10)

    choices = ['Rock', 'Paper', 'Scissors']

    for choice in choices:
        button = tk.Button(
            root, text=choice, font=("Helvetica", 12),
            command=lambda c=choice: play_game(c)
        )
        button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
