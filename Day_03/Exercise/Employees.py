class Employee:
    """Class representation for employee data"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)



class Recruiter(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
    def recruit(self):
        self.add_work("recruit")
class Developer(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
    def code(self):
        self.add_work("code")

class Manager(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
    def manage(self):
        self.add_work("manage")

employee1 = Recruiter("Richard", "1234")
print("Employee 1 Name:", employee1.name)
employee1.add_work("Create Slides")

employee2 = Manager("Loraine", "5678")
print("Employee 2 Name:", employee1.name)
employee2.add_work("Manage the hotel")
employee2.manage()

employee1 = Recruiter("Richard", "1234")
print("Employee 1 Name:", employee2.name)
employee1.add_work("Create Slides")
employee1.recruit()

employee3 = Developer("Lorenzo", "666")
print("Employee 3 Name:", employee3.name)
employee3.add_work("Make a website")
employee3.code()

























