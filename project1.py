import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    try:
        if float(num2.get()) == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Arithmetic Calculator")
root.geometry("300x300")
root.resizable(False, False)

num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

tk.Label(root, text="Enter first number:").pack(pady=5)
tk.Entry(root, textvariable=num1).pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
tk.Entry(root, textvariable=num2).pack()

tk.Label(root, text="Result:").pack(pady=5)
tk.Entry(root, textvariable=result, state='readonly').pack()

tk.Button(root, text="Add", width=10, command=add).pack(pady=5)
tk.Button(root, text="Subtract", width=10, command=subtract).pack(pady=5)
tk.Button(root, text="Multiply", width=10, command=multiply).pack(pady=5)
tk.Button(root, text="Divide", width=10, command=divide).pack(pady=5)

root.mainloop()
