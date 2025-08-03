

# #Ask the user for an input
# user_input = input ("Enter number: ")
# #If user enters a valid number
# user_input = int(user_input)
# print(user_input + 1)
# #Else
# print("Please enter a valide number")

user_input = input ("Enter number: ").strip().replace(",","").replace(" ","")
digits = user_input.split()
user_input = "".join(digits)
if user_input.isnumeric():
    user_input = int(user_input)
 #   print(user_input + 1)
    print("This is a valid number")
else:
    print("Please enter a valid number")






