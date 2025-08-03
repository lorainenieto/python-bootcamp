from tkinter.constants import COMMAND


def spend(expenses):
    expense = int(input("How many expense: "))
    for attendee in range(expense):
        cost = str((input("Add cost: ")))
        expenses.append(cost)



def refund (expense):
    expense.pop(-1)
def show(expense):
    for exp in expense:
       print(exp)
def save(expenses):
    """save the expenses in the filepath  """
    filepath = input("Filepath: ")
    with open(filepath,"w") as file:
        for expense in expenses:
            file.write(str(expense)+"\n")
def main():
    current_expense =[]
    command = str(input("Enter command: "))
    while command:
        if command == "spend":
            spend(expenses=current_expense)
        elif command == "refund":
            refund(current_expense)
            print("Refunding...")
        elif command == "show":
            show(current_expense)
            print(sum(current_expense))
        elif command == "save":
            save(current_expense)
        else:
            print("Enter a valid command next time.")

        command = input("Command: ")


main()















