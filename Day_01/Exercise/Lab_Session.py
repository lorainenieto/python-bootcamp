"""
Multiplication Table
Ask the user for an integer input
1 number = int(input("Pick a number: "))
Print the multiplication table for that number
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
…
3 x 10 = 30
"""

numbers = int(input("Give a number: "))
for number in range(11):
    result = numbers*number
    print(f"{numbers} x {number} = {result}")







