#Ask tge user input for a color
color_input = input("Enter a color: ")

#Print the following depending on the color input
if color_input == "green":
    print("Go")
elif color_input == "yellow":
    print("Wait")
elif color_input == "red":
    print("stop")
else:
    print("Malfunction")

color_input2 = input("Enter a color: ")
match color_input2:
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case "red":
        print("stop")
    case _:
        print("Malfuntion")





