# attendance_names = set()
#
# attendance_count = int (input("Attendance count: "))
# #Do this for as many attendees expected
# attendee_name = input("Attendee name: ")
# #Add attendee_name to attendee_names
# #Remove your name from attendees (if there)
# print(attendee_names)


attendance_names = set()
my_name = "loraine"
attendance_count = int (input("Attendance count: "))
for attendee in range(attendance_count):
    attendee_name = str((input("Attendee name: ")))
    attendance_names.add(attendee_name)
attendance_names.discard(my_name)
winner = attendance_names.pop()
print(f"The winner is {winner}!")

































