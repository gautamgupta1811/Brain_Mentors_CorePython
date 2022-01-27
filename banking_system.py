class Bank:
    def __init__(self):
        self.code = ifsc
        self.address = address
        self.number = number
        self.customer_count = 0

    def inc_customer_count(self):
        self.customer_count += 1

    def daily_revenue(self):
        pass


class Customer:
    def __init__(self):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self):
        pass

    def widthdraw(self):
        pass


class Loan:
    def __init__(self):
        pass

    def deposit(self):
        pass