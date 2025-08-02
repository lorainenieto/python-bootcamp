correct_password = "pass"

password = input("Enter password:").lower()
while password != correct_password:
    password = input("Try again. Enter password:")
print("Correct")