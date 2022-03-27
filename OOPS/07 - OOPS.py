# bank account --> name, acc_num, balance, type
# widthdraw, deposit


class BankAccount:
    def __init__(self, name, acc_num, balance, type):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance
        self.type = type


cust_1 = BankAccount("ajay", 1234, 12000, "S")
cust_2 = BankAccount("vijay", 2345, 12000, "S")
cust_3 = BankAccount("Virat", 3456, 35000, "C")

print(cust_1.__dict__)
print(cust_2.__dict__)
print(cust_3.__dict__)


