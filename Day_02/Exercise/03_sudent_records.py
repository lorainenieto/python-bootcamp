student_names = ("Juan", "Maria", "Joseph")
student_scores = (70,90,81)

"""
Print the student scores and names in the following format 
Student records:
Juan score 70 in the exam
Maria score 90 in the exam
Joseph score 81 in the exam

"""
for student_name, student_score in zip(student_names, student_scores):
    print(f"Student Record: {student_name} scored {student_score} in the exam")






