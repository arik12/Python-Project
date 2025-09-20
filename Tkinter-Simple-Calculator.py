
# -----------------------------------
# Simple Python Calculator using Tkinter
# -----------------------------------

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")

# First Number
tk.Label(root, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_num1 = tk.Entry(root, width=15, font=("Arial", 12))
entry_num1.grid(row=0, column=1, padx=10, pady=10)

# Second Number
tk.Label(root, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num2 = tk.Entry(root, width=15, font=("Arial", 12))
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operator
tk.Label(root, text="Enter Operator (+,-,*,/):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_op = tk.Entry(root, width=15, font=("Arial", 12))
entry_op.grid(row=2, column=1, padx=10, pady=10)

# Label to display result
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform calculation
def calculate():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        op = entry_op.get()

        # Perform calculation based on operator
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result = "Error: Division by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid Operator!"

        # Display result on the label
        label_result.config(text=f"{num1} {op} {num2} = {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers!")

# Button to calculate
tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
