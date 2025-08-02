items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    if item == item_to_find:
        print("Item found")
        break



items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = input("Enter food:")

for item in items:
    if item == item_to_find:
        print("Item found")
        break
