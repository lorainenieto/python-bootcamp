# attendance_names = []
# attendee_count = int(input("Attendee count: "))
# #Do this fopr as many attendees expected
# attendee_name = input("Attendee name: ")
# #Add attendee_name to antendee_names
#

# attendance_names = [ ]
# attendee_count = int(input("Attendee count: "))
# for attendee in range(attendee_count):
#     attendee_name = str((input("Attendee name: ")))
#     attendance_names.append(attendee_name)
# for attendee in sorted(attendance_names):
#     print(attendee)


# attendance_names = [ ]
# my_name = "loraine"
# attendee_count = int(input("Attendee count: "))
# for attendee in range(attendee_count):
#     attendee_name = str((input("Attendee name: ")))
#     attendance_names.append(attendee_name)
# if my_name in attendance_names:
#     attendance_names.remove(my_name)
# for attendee in sorted(attendance_names):
#     print(f" {attendee}, {my_name} is removed")










attendance_names = [ ]
my_name = "loraine"
attendee_count = int(input("Attendee count: "))
for attendee in range(attendee_count):
    attendee_name = str((input("Attendee name: ")))
    attendance_names.append(attendee_name)
if my_name in attendance_names:
    attendance_names.remove(my_name)
    print(f" {attendance_names}, {my_name} is removed")
attendance_names.pop(-1)
print(attendance_names)





