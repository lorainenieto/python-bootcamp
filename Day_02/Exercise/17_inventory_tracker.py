
import json


def create(inventory, item):
    """Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)
def read(inventory, index):
    """Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]
def update(inventory, index, detail_key, detail_value):
    """Change/add the key and value to the given index in inventory"""
    inventory[index][detail_key] = detail_value
def delete(inventory, index):
    """Remove item (dict) in the given index (int) of inventory"""
    inventory.pop(index)
def show(inventory):
    """Print the items and their details line-by-line"""
    print(inventory)
    for item in inventory:
        for key, values in item.inventory():
            print(f"\t {key}: {values}")

def save(inventory, filepath):
    """save the inventory to the filepath"""
    with open(filepath,"w") as file:
        json.dump(inventory, file)
def load(filepath):
    with open(filepath, "r") as file:
        data=json.load(file)
        return data


def main():
    current_inventory = []
    command = input("Command: ")

    while command:
        if command == "create":
            create(inventory=current_inventory)
            name = input("Item name: ")
            quantity = input("Quantity: ")
            item = {"name": name, "Quantity": quantity}
            create(current_inventory, item)
        elif command == "read":
            read(current_inventory)
            index = int(input("Index: "))
            item = read(current_inventory, index)
        elif command == "update":
            update(current_inventory)
        elif command == "delete":
            index = int(input("Index: "))
            delete(current_inventory, index)
        elif command == "show":
            show(current_inventory)
        elif command == "save":
            save(current_inventory, input("Filepath: "))
        elif command == "load":
            filename = input("Filepath: ")
            inventory = load(filename)
            current_inventory.extend(inventory)
        command = input("Command: ")



main()













