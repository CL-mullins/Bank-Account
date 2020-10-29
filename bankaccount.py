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
        return balance - amount
        balance = balance - amount
        print(f'Amount Deposited: ${amount}')

    def get_balance(self):
        print(f'Hello, {full_name}')
        printf(f'Your balance is {balance}')

    def add_interest():
        interest = balance *  0.00083
        balance = balance + interest
        return balance



SamJohnson = BankAccount('Sam Johnson', 82712391, 38914091, 500.00)
print("Hello, I'm Banksy, your personal banking assistant!")

SamJohnson.deposit(6)