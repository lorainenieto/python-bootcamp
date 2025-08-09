import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("1200x400")

# label = tkinter.Label(root, text = "Hello")
# label.pack()
#
# new_label =tkinter.Label(root, text = "Another one")
# new_label.pack()

message = """
 hello world. 
 i am loraine
"""
label = tkinter.Label(root, text = message)
label.pack()

text = "Hello world, I am Loraine Nieto. I am studying Python right now yehey!"
root.mainloop()









