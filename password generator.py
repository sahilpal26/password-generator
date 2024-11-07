import random
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        maximum_length = int(length_entry.get())  
        if maximum_length <= 0:
            raise ValueError("Length must be greater than zero")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")
        return

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    locase_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upcase_character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    combined = digits + locase_character + upcase_character + symbols
    password_random = []

    for x in range(0, maximum_length):
        y = random.choice(combined)
        password_random.append(y)

    password_final = "".join(password_random)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_final)

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Password Length Label
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

# Password Length Entry
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password Result Label
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

# Password Result Entry
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Start the application
root.mainloop()