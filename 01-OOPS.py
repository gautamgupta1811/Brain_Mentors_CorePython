# it is a programming paradigm in which program is represented in form of classes and object
# class --> type
# class is a user defined datatype having its own variables and functions. It does not occupy any memory unless an
# object is instasited

# object --> it is an instance class

# emp --> id, name, salary, post

# inheritance, abstraction, encapsulation, polymorphsim

class Employee:
    def __init__(self, name, id, salary, post):
        self.name = name
        self.id = id
        self.salary = salary
        self.post = post

    def inc_sal(self):
        self.salary += 0.1 * self.salary

# emp
emp = Employee("Ajay", 1234, 12098, "manager")
print(emp.name)
print("Pre salary", emp.salary)
print(emp.id)
print(emp.post)
print("="*50)
print(emp.__dict__)

emp.inc_sal()
print("Post salary", emp.salary)

# emp_1
emp_1 = Employee("Vijay", 1235, 12980, "coder")
print(emp_1.name)
print(emp_1.salary)
print(emp_1.id)
print(emp_1.post)

## name, salary, id, post
