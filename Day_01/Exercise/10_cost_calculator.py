# #Ask the user for the following inputs:
# item_1_price = int(input("Give me the item price 1:"))
# item_2_price = int(input("Give me the item price 2:"))
# item_3_price = int(input("Give me the item price 3:"))
#
# total = item_1_price + item_2_price + item_3_price
# print(f"{item_1_price} + {item_2_price} + {item_3_price} = {total}")
#
# item_quantity_1 = int(input("Give me the quantity for 1:"))
# item_quantity_2 = int(input("Give me the quantity for 2:"))
# item_quantity_3 = int(input("Give me the quantity for 3:"))


#################################################################
"""Ask the user how many  items to purchase
item_count =int(input("Enter item count: "))
total = 0

#Fore every item in range of item_count, ask for an item price
item_price = int(input("Enter item count: "))

#Add the item price to the total price
print(total)
"""

item_count =int(input("Enter item count: "))

for item in range(item_count):
    item_price = int(input("Enter item price: "))
    total = total + item_price
    if total <=600:
        continue
    print(total)













