class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal not possible"
        else:
            self.balance = self.balance - amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

p1 = BankAccount()
p2 = BankAccount()

print("P1 balance:", p1.withdraw(12000))
print("P2 balance:", p2.deposit(23000))

p1.deposit(1234)
p2.withdraw(1234)
