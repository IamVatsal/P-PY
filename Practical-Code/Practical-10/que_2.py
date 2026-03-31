import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("380x100")
tk.Label(root, text="Enter Weight in Kg: ").grid(row=0, column=0, columnspan=1)
weight = tk.StringVar()
tk.Entry(root, textvariable=weight).grid(row=0, column=1, columnspan=1)
result_gram = tk.StringVar()
result_pound = tk.StringVar()
result_ounce = tk.StringVar()
def convert():
    w = float(weight.get())
    result_gram.set(f"{w*1000}")
    result_pound.set(f"{w*2.20462}")
    result_ounce.set(f"{w*35.274}")

tk.Button(text="Convert", command=lambda :convert()).grid(row=0, column=2, columnspan=1)

tk.Label(text="Weight in Gram: ").grid(row=2, column=0, columnspan=1)
tk.Label(text="Weight in Pound: ").grid(row=2, column=1, columnspan=1)
tk.Label(text="Weight in Ounce: ").grid(row=2, column=2, columnspan=1)
tk.Entry(root, textvariable=result_gram, state="readonly").grid(row=3, column=0, columnspan=1)
tk.Entry(root, textvariable=result_pound, state="readonly").grid(row=3, column=1, columnspan=1)
tk.Entry(root, textvariable=result_ounce, state="readonly").grid(row=3, column=2, columnspan=1)

tk.mainloop()