import tkinter as tk

root = tk.Tk()
root.title("Font Dialog")

# -------- LEFT: Font list --------
font_frame = tk.Frame(root)
font_frame.grid(row=0, column=0, padx=10)

tk.Label(font_frame, text="Font").pack()

font_list = tk.Listbox(font_frame, height=6)
fonts = ["Times", "Verdana", "Arial", "Courier"]
for f in fonts:
    font_list.insert(tk.END, f)

font_list.pack()

# -------- MIDDLE: Font Style --------
style_frame = tk.Frame(root)
style_frame.grid(row=0, column=1, padx=10)

tk.Label(style_frame, text="Font Style").pack()

font_style = tk.StringVar(value="Regular")
styles = ["Regular", "Italic", "Bold", "Bold Italic"]

for s in styles:
    tk.Radiobutton(style_frame, text=s, variable=font_style, value=s).pack(anchor="w")

# -------- RIGHT: Font Size --------
size_frame = tk.Frame(root)
size_frame.grid(row=0, column=2, padx=10)

tk.Label(size_frame, text="Font Size").pack()

scrollbar = tk.Scrollbar(size_frame)
scrollbar.pack(side="right", fill="y")

size_list = tk.Listbox(size_frame, yscrollcommand=scrollbar.set, height=6)
for i in range(1, 101):
    size_list.insert(tk.END, i)

size_list.pack(side="left")
scrollbar.config(command=size_list.yview)

# -------- SAMPLE TEXT --------
sample = tk.Label(root, text="Sample Text", relief="sunken")
sample.grid(row=2, column=0, columnspan=3, pady=10)

# -------- APPLY FUNCTION --------
def apply_font():
    try:
        selected_font = font_list.get(tk.ACTIVE)
        selected_size = int(size_list.get(tk.ACTIVE))
        selected_style = font_style.get()

        weight = "normal"
        slant = "roman"

        if "Bold" in selected_style:
            weight = "bold"
        if "Italic" in selected_style:
            slant = "italic"

        sample.config(font=(selected_font, selected_size, weight, slant))

    except:
        print("Select all options properly")

tk.Button(root, text="Apply", command=apply_font).grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()