import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(temp_input.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == to_unit:
            result.set(f"{temp:.2f} {to_unit}")
            return

        if from_unit == "Celsius":
            celsius = temp
        elif from_unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = temp - 273.15

        if to_unit == "Celsius":
            converted = celsius
        elif to_unit == "Fahrenheit":
            converted = (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            converted = celsius + 273.15

        result.set(f"{converted:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid temperature.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.resizable(False, False)

units = ["Celsius", "Fahrenheit", "Kelvin"]

temp_input = tk.StringVar()
from_var = tk.StringVar(value="Celsius")
to_var = tk.StringVar(value="Fahrenheit")
result = tk.StringVar()

tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=temp_input, font=("Arial", 12), width=15, justify="center").pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0, padx=5)
from_menu = ttk.Combobox(frame, textvariable=from_var, values=units, state="readonly")
from_menu.grid(row=0, column=1)

tk.Label(frame, text="To:").grid(row=1, column=0, padx=5, pady=5)
to_menu = ttk.Combobox(frame, textvariable=to_var, values=units, state="readonly")
to_menu.grid(row=1, column=1)

tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12)).pack(pady=10)
tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue").pack(pady=10)

root.mainloop()
