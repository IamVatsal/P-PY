import tkinter as tk
import sqlite3

cnx = sqlite3.connect('student_details.db')
cursor = cnx.cursor()

query = "DROP TABLE IF EXISTS student_details"
cursor.execute(query)
cnx.commit()

query = """
CREATE TABLE IF NOT EXISTS student_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    enrollment_number TEXT,
    student_name TEXT, 
    gender TEXT,
    address TEXT,
    branch TEXT,
    mobile_number TEXT,
    email TEXT
)
"""
cursor.execute(query)

def submit_form():
    enrollment = enrollment_entry.get()
    name = name_entry.get()
    gender = gender_var.get()
    address = address_entry.get()
    branch = branch_var.get()
    mobile = mobile_entry.get()
    email = email_entry.get()

    query = """INSERT INTO student_details (enrollment_number, student_name, gender, address, branch, mobile_number, email)
               VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(query, (enrollment, name, gender, address, branch, mobile, email))
    cnx.commit()
    print("Form Submitted Successfully!")

def view_form():
    query = "SELECT * FROM student_details"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
 
# Initialize the main application window
root = tk.Tk()
root.title("Register Form")
root.geometry("400x400")

# Create labels and entry fields for user input
tk.Label(root, text="Enter Enrollment Number:").grid(row=0, column=0, padx=10, pady=10)
enrollment_entry = tk.Entry(root)
enrollment_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

tk.Label(root, text="Enter Name:").grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

gender_var = tk.StringVar()

tk.Label(root, text="Select Gender:").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, padx=10, pady=10)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Enter Address:").grid(row=3, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

branches = ["Computer Science", "Mechanical", "Electrical", "Civil"]
tk.Label(root, text="Select Branch:").grid(row=4, column=0, padx=10, pady=10)
branch_var = tk.StringVar()
branch_menu = tk.OptionMenu(root, branch_var, *branches)
branch_menu.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

tk.Label(root, text="Enter Mobile Number:").grid(row=5, column=0, padx=10, pady=10)
mobile_entry = tk.Entry(root)
mobile_entry.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

tk.Label(root, text="Enter Email:").grid(row=6, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=6, column=1, padx=10, pady=10, columnspan=2)


tk.Button(root, text="Submit", command=submit_form).grid(row=7, column=1, padx=10, pady=20)
tk.Button(root, text="View", command=view_form).grid(row=7, column=2, padx=10, pady=20)

tk.mainloop()