import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create a label to display the result
result_label = tk.Label(window, text="Make your choice!", font=("Helvetica", 14))
result_label.pack(pady=20)

# Create buttons for rock, paper, and scissors
rock_button = tk.Button(window, text="Rock", width=12, command=lambda: play_game('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=12, command=lambda: play_game('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=12, command=lambda: play_game('scissors'))
scissors_button.pack(pady=5)

# Run the main loop
window.mainloop()
