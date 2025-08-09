import tkinter


root = tkinter.Tk()



# instruction = tkinter.label
# instruction.pack()
user_input = tkinter.StringVar(root, value="Enter your password.")
label = tkinter.Label(root, textvariable=user_input)
label.pack()
entry = tkinter.Entry(root)
entry.pack()


def show_input(event):
    given_text = entry.get()
    user_input.set(given_text)

    correct_password = "password"
    if given_text == correct_password:
        user_input.set("Access Granted!")
    else:
        user_input.set("Access Denied")

root.bind("<Return>", show_input)
root.bind("<space>", show_input)
root.mainloop()