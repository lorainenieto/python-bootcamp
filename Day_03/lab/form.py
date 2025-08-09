import json
import tkinter
root = tkinter.Tk()


################## name
name_input = tkinter.StringVar(root, value="Name")
label = tkinter.Label(root, textvariable=name_input)

label.pack()
entry = tkinter.Entry(root)
entry.pack()

################# age
age_input = tkinter.StringVar(root, value="Age")
label = tkinter.Label(root, textvariable=age_input)

label.pack()
entry = tkinter.Entry(root)
entry.pack()

################# Theme

label = tkinter.Label(root, text="Preferred Theme")
label.pack()

radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
root, text="Light", variable=radio_var, value="Light")
radio1.pack()
radio2 = tkinter.Radiobutton(
root, text="Dark", variable=radio_var, value="Dark")
radio2.pack()

################# checkbox

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Subscribe to Newsletter",
    variable=check_value)
checkbox.pack()

################# Slider

label = tkinter.Label(root, text="Rate")
label.pack()

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_=0,
    to=10,
    orient="horizontal",
    variable=slider_value
)
slider.pack()

def submit(event=None):
    data={
        "Name": f"{name_input.get()}",
        "Age": age_input.get(),
        "Theme": f"{radio_var.get()}",
        "Subscribe": f"{check_value.get()}",
        "Rating": f"{slider_value.get()}"
    }
    with open("user.json","w") as file:
        json.dump(data,file)

################# Button
button = tkinter.Button(root, text="Submit", command=submit)
button.pack()





# root.bind("<Return>", show_input)
# root.bind("<space>", show_input)
root.mainloop()

















