ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k']
print(ranks[1])
print(ranks[-3])

ranks[2] = "hi"
print(ranks)
del ranks[-1]


letters = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k')
#tuples are not editable or deletable
try:
letters[-2] = "xx"
print(letters)


student_data = [("Maria", 90), ("Pedro", 30), ("Bax", 10)]
first_record = student_data[0]
first_record_score = first_record[1]
print(first_record)
print(first_record_score)
first_record = student_data[0][1]
print(first_record)



