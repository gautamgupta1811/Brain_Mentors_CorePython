class Employee:
    # constructor --> it is a function which all itself at time of
    # object instantiation
    def __init__(self, id, name, salary, age, post):
        self.id_ = id
        self.name = name
        self.salary = salary
        self.age = age
        self.post = post
        self.experience = 0

    def inc_experience(self, project_completed):
        self.experience += project_completed
        print(self.experience)

emp_1 = Employee(1, "Ajay", 12000, 25, "Manager")
emp_2 = Employee(2, "Vijay", 12000, 22, "Tech Consultant")

print(emp_1.__dict__)
print(emp_2.__dict__)

emp_1.inc_experience(3)
print(emp_1.__dict__)
print(emp_2.__dict__)
