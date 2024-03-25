class BankAccount(object):
    balance=0
    ac_name=("")
    def __init__(self):
        pass

    def withdrawn(self,amount):
        self.balance=self.balance-amount
        return self.balance

    def transfer(self,amount):
        self.balance=self.balance-amount
        return self.balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def show_balance(self):
        print("the account details are:Name-",self.ac_name,"Balance:",self.balance)

    #creating instances of bank account
ac1=BankAccount()
ac1.balance=100
ac1.ac_name="Alex"
ac1.show_balance()