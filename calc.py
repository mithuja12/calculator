import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

expression = ""
equation = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Display
entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Segoe UI", 24),
    justify="right",
    bg="#252526",
    fg="white",
    bd=0
)
entry.grid(row=0, column=0, columnspan=4,
           sticky="nsew", padx=10, pady=10,
           ipady=20)

# Button style
btn_font = ("Segoe UI", 16)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for text, row, col in buttons:

    color = "#3e3e42"
    fg = "white"

    if text in ['/', '*', '-', '+', '=']:
        color = "#0078D7"

    btn = tk.Button(
        root,
        text=text,
        font=btn_font,
        bg=color,
        fg=fg,
        bd=0,
        activebackground="#005A9E",
        activeforeground="white",
        command=equal if text == '=' else lambda t=text: press(t)
    )

    btn.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=5,
        pady=5
    )

# Clear button
clear_btn = tk.Button(
    root,
    text="C",
    font=btn_font,
    bg="#D13438",
    fg="white",
    bd=0,
    command=clear
)

clear_btn.grid(
    row=5,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
)

# Responsive grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()