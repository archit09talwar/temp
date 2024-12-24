import tkinter as tk

def on_button_click(value):
    print(f"Button {value} clicked")

root = tk.Tk()
root.title("3x3 Button Grid")

button_width = 10
button_height = 3

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=f"{i*3 + j + 1}", width=button_width, height=button_height,
                           command=lambda value=i*3 + j + 1: on_button_click(value))
        button.place(x=j*button_width*10, y=i*button_height*20)
        row.append(button)
    buttons.append(row)
    # here is for the last row with extra button

last_button_width = 7

last_row = []
for j in range(4):
    button = tk.Button(root, text=f"{j + 10}", width=last_button_width, height=button_height,
                       command=lambda value=j + 10: on_button_click(value)) 
    button.place(x=j*last_button_width*10, y=3*button_height*20)
    row.append(button)
buttons.append(last_row)

root.geometry(f"{button_width*30}x{button_height*60}")
root.mainloop()