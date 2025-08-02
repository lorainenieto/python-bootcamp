#Ask the user for their profile
role = input("Enter role: ").lower()
""" 
#If role is "admin" or role is "edit or", print the following
print("Edit Access Enabled")

#Else, print "Access Denied"
print("Edit not allowed")
"""
if role == "editor" or "admin":
    print("Access granted")
else:
    print("Access Denied")














