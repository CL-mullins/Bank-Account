class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self,amount):
        self.balance = amount + self.balance
        print(f'Amount Deposited: ${amount}') 

    def widthdraw(self,amount):
        self.balance = self.balance - amount
        print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        print(f'Hello, {self.full_name}')
        print(f'Your balance is {self.balance}')

    def add_interest():
        interest = balance *  0.00083
        balance = balance + interest
        return balance



SamJohnson = BankAccount('Sam Johnson', 82712391, 38914091, 500.00)
print("Hello, I'm Banksy, your personal banking assistant!")

SamJohnson.deposit(6.53)
SamJohnson.widthdraw(3.53)
SamJohnson.get_balance()