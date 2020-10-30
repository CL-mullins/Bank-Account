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
        if amount > self.balance:
            self.balance = self.balance - amount
            print("Insufficient Funds")
            self.balance = self.balance - 10
            print(f'Amount Withdrawn ${amount}')
            #Overdraft fee

        else:
            self.balance = self.balance - amount
            print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        print(f'Hello, {self.full_name}')
        print(f'Your balance is ${round(self.balance,2)}')

    def add_interest(self):
        interest = self.balance *  0.00083
        self.balance = self.balance + interest

    def print_receipt(self):
        print('              ')
        print(self.full_name)
        #how do you change the characters in a string
        self.account_number = self.account_number.replace("4","*")
        print(f'Account number: {self.account_number}')
        print(f'Routing number: {self.routing_number}')
        print(f'Balance: ${round(self.balance,2)}')



SamJohnson = BankAccount('Sam Johnson', '44442391', 38914091, 500.00)
RickJameson = BankAccount('Rick Jameson', '44449381',38914091,250)
JaneDoe = BankAccount('Jane Doe', '44441238',38914091, 1000)
JohnDoe = BankAccount('John Doe','44446220', 38914091, 25)

print('             ')
print("Hello, I'm Banksy, your personal banking assistant!")
print('Please enter')

SamJohnson.get_balance()
SamJohnson.deposit(6.53)
SamJohnson.widthdraw(600)
SamJohnson.add_interest()
SamJohnson.get_balance()

SamJohnson.print_receipt()
