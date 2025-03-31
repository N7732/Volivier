class Bank:
    def __init__(self,Account_name,balance):
        self.Account_name=Account_name
        self.balance=balance
class INITIAL(Bank):
    def __init__(self, Account_name, balance,initial_amount):
        super().__init__(Account_name, balance)
        self.initial_amount=initial_amount
    def deposit1(self):
     d=self.balance+self.initial_amount
     return d
class Saving(INITIAL):
    def __init__(self,Account_name,balance,initial_amount,amount,rate=5):
        super().__init__(Account_name,balance,initial_amount)
        self.amount=amount
        self.rate=rate

    def deposit(self):
        interest=self.amount*(self.rate/100)
        f=self.amount + interest
        c=self.deposit1()
        return f+c

customer1=Bank("EQUITY2025",1000)
print(f"ACCOUNT NAME IS:{customer1.Account_name}")
customer1=INITIAL("EQUITY2025",1000,20000)
print(f"balance and initial amount :{customer1.deposit1()}")
customer1=Saving("EQUITY2025",1000,20000,5000)
print(f"Total amount :{customer1.deposit()}")



