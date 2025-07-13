import tkinter as tk
import random
from tkinter import messagebox

secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    guess = entry.get()

    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            result_label.config(text="⚠ Enter a number between 1 and 100.")
            return
        attempts += 1

        if guess < secret_number:
            result_label.config(text="🔼 Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="🔽 Too high! Try again.")
        else:
            messagebox.showinfo("🎉 Correct!", f"You guessed it in {attempts} attempts!\nThe number was {secret_number}.")
            reset_game()
    except ValueError:
        result_label.config(text="❗ Please enter a valid number.")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Game reset. Try to guess the new number!")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="🎯 Guess a number between 1 and 100:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
entry.pack()

tk.Button(root, text="Submit Guess", command=check_guess, font=("Arial", 11)).pack(pady=10)
tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 11)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
