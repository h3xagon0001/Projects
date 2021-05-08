import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=150, height=100)
canvas.grid(columnspan=3, rowspan=3)

label = tk.Label(root, text="Hello World")
label.grid(columnspan=3, column=0, row=0)

buttonText = tk.StringVar()
button = tk.Button(root, textvariable=buttonText, command=lambda:print("You clicked a button."),bg="#A7C7E7", height=2, width=10)
buttonText.set("Click Me!")
button.grid(column=1, row=1)

root.mainloop()
