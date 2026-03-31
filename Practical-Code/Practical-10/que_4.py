import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Register Form")
root.geometry("400x300")

# Create labels and entry fields for user input
tk.Label(root, text="Enter Enrollment Number:").grid(row=0, column=0, padx=10, pady=10)
enrollment_entry = tk.Entry(root)
enrollment_entry.grid(row=0, column=1, padx=10, pady=10)