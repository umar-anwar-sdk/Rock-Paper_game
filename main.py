import random
import tkinter as tk


def check_winner(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    if user_choice == computer_choice:
        result_label.config(text=f"Computer's choice: {computer_choice}\nIt's a Tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text=f"Computer's choice: {computer_choice}\nYou Win!")
    else:
        result_label.config(text=f"Computer's choice: {computer_choice}\nYou Lose!")


def play():
    user_choice = user_input.get()
    if user_choice not in ['Rock', 'Paper', 'Scissors']:
        result_label.config(text="Invalid input. Please choose Rock, Paper, or Scissors.")
    else:
        check_winner(user_choice)

    play_button.config(state=tk.DISABLED)
    play_again_button.config(state=tk.NORMAL)


def play_again():
    user_input.delete(0, 'end')
    result_label.config(text="")
    play_button.config(state=tk.NORMAL)
    play_again_button.config(state=tk.DISABLED)


# Creating the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# User input entry field
user_input = tk.Entry(root, width=50, )
user_input.pack()

# Button to play
play_button = tk.Button(root, text="Play", width=20, height=5, command=play)
play_button.pack()

# Label for displaying results
result_label = tk.Label(root, text="", width=50, height=5, fg="blue", font=("Arial", 12))
result_label.pack()

# Button to play again
play_again_button = tk.Button(root, text="Play Again", width=20, command=play_again, state=tk.DISABLED)
play_again_button.pack()

root.mainloop()
