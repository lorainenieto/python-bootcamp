


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.a = 1
        self.b = 2
        self.c = 3


    def sleep(self):
        print("I will sleep for eight hours")

    def introduce(self):
        print(f"Hello, my names is {self.first_name} {self.last_name}. I am a {self.level} student")

class Student(Person):
    def __init__(self, first_name, last_name, level):
        super().__init__(first_name, last_name)
        self.level = level
    def introduce(self):
        return super().introduce() + f"I'm a self {self.level} student"

student = Student("John", "Cena", "3rd year high school")
print(student.sleep())











