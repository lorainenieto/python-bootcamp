#Range minimum and maximum bounds
min_number = 0
max_number = 100

#Enter user input
number = int(input("Give me a number:"))

#Notify user if the number is a valid score
#Change the variable value here
valid_score = 0 <= number <= 100
print("Valid Score: ", valid_score)