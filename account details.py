class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno
    def debit(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"{amount} is debited, balance is {self.get_bal()}")
        else:
            print("Insufficient funds")
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is credited, balance is {self.get_bal()}")
    def get_bal(self):
        return self.balance
acc1 = Account(1000, 101)
acc1.credit(500)  
acc1.debit(300)   
acc1.debit(1500)  

