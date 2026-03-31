import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("250x150")
tk.Label(root, text="Enter Num 1: ").grid(row=0, column=0, columnspan=1)
n1 = tk.StringVar()
n2 = tk.StringVar()
tk.Entry(root, textvariable=n1).grid(row=0, column=1, columnspan=2)
tk.Label(root, text="Enter Num 2: ").grid(row=1, column=0, columnspan=1)
tk.Entry(root, textvariable=n2).grid(row=1, column=1, columnspan=2)
op = tk.StringVar()
tk.Button(text="+", command=lambda :op.set("+")).grid(row=3, column=1)
tk.Button(text="-", command=lambda :op.set("-")).grid(row=3, column=2)
tk.Button(text="*", command=lambda :op.set("*")).grid(row=4, column=1)
tk.Button(text="/", command=lambda :op.set("/")).grid(row=4, column=2)

result = tk.StringVar()

def cal():
    num1 = float(n1.get())
    num2 = float(n2.get())
    opr = op.get()

    if opr == "+":
        result.set(f"Ans : {num1+num2}")
    elif opr == "-":
        result.set(f"Ans : {num1-num2}")
    elif opr == "*":
        result.set(f"Ans : {num1*num2}")
    elif opr == "/":
        result.set(f"Ans : {num1/num2}")

tk.Button(text="=", command=cal).grid(row=4, column=0)
tk.Label(textvariable=result).grid(row=5, column=0, columnspan=3)
    
tk.mainloop()