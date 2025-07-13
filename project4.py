import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("400x400")

# List to hold tasks
tasks = []

# Add task
def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty.")
    else:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)

# Remove selected task
def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")

# Update task list display
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI Components
task_entry = tk.Entry(root, width=30, font=('Arial', 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Selected Task", width=20, command=remove_task)
remove_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=45, height=10, font=('Arial', 12))
task_listbox.pack(pady=10)

# Scrollbar for listbox
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Run the app
root.mainloop()

