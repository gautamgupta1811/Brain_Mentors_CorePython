class A:
    def __init__(self):
        self.a = 10

# camel case --> BigClass
# function name: small case seperated by _
class B(A):  # class B inherits A
    def __int__(self):
        super().__init__()
        self.b = 20


obj_b = B()
print(obj_b.a)

#  PEP 8
