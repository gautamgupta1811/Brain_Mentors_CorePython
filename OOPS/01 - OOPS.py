# procedural, functional programming

# single variable cannot be used multiple times

# human --> 2 eyes IRIS structure is different
#         --> Fingerprints are unique
# human has completely unique features

# common structure --> blue print --> class
# instance of classes --> object
# name --> CamelCase
class Employee:
    # variables  --> data members
    name = "Ajay"
    post = "Manager"
    salary = 10000
    emp_id = 12
    age = 25
    # functions --> member functions
    # def sal_inc(self, inc_percentage):
    #     salary = salary + (salary * inc_percentage)

emp = Employee()
print(emp)
print(emp.emp_id)
print(emp.age)
