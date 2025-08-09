
############################ Properties ###############################################
import tkinter
from tkinter import font

root = tkinter.Tk()
all_fonts = font.families()

message = """
 hello world. 
 i am loraine
"""
label = tkinter.Label(
    root,
    text = message,
    font = ("Arial", 14, "bold italic"),
    fg="green",
    bg="yellow",
    width= 100,
    height=20,
    padx =10,
    pady=200
)




left = tkinter.Label(root, text = "Left", padx =5, bg="blue")
left.pack(side = "left")

right = tkinter.Label(root, text = "Right", padx =5, bg="red")
right.pack(side = "right")



text = "Hello world, I am Loraine Nieto. I am studying Python right now yehey!"
root.mainloop()


