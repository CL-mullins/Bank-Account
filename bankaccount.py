class BankAccount:
    #Creates a bank account class with 5 methods for various functions defined below
    def __init__(self, full_name, account_number, routing_number, balance):
        #Initializes the bank account class with the user's name, randomized account number, and balance.
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
    

    def deposit(self,amount):
        #Function that deposits money into the specified user's bank account. Increasing their balance by a specified amount.
        #Function prints bank account balance in dollar measure
        self.balance = amount + self.balance
        print(f'Amount Deposited: ${amount}') 

    def widthdraw(self,amount):
        #Function that withdraws money from the user's bank account. If the withdrawal amount is over the user's current balance, the amount is withdrawn
        #however, there will be an insufficient funds statement and an overdraft fee of $10 applied.
        if amount > self.balance:
            self.balance = self.balance - amount
            print("Insufficient Funds")
            self.balance = self.balance - 10
            print(f'Amount Withdrawn ${amount}')
            #Overdraft fee applied here

        else:
            self.balance = self.balance - amount
            print(f'Amount Withdrawn: ${amount}')
            #Situation where the balance exceeds withdrawn amount

    def get_balance(self):
        #Prints a welcome message, then prints the balance of the user's account rounded to a dollar value
        print(f'Hello, {self.full_name}')
        print(f'Your balance is ${round(self.balance,2)}')

    def add_interest(self):
        #Adds a fixed amount of interest to the users account
        interest = self.balance *  0.00083
        self.balance = self.balance + interest

    def print_receipt(self):
        #Reports various attributes of the user's account including account number, name, balance, and routing number
        print('              ')
        print(self.full_name)
        censor = "****"
        print(f'Account number: {censor + self.account_number[4:9]}')
        print(f'Routing number: {self.routing_number}')
        print(f'Balance: ${round(self.balance,2)}')


#Initialization of various different accounts
SamJohnson = BankAccount('Sam Johnson', '31232391', 38914091, 500.00)
RickJameson = BankAccount('Rick Jameson', '41929381',38914091,250)
JaneDoe = BankAccount('Jane Doe', '12391238',38914091, 1000)
JohnDoe = BankAccount('John Doe','31906220', 38914091, 25)

#Chatbot functionality
print('             ')
print("Hello, I'm Banksy, your personal banking assistant!")
print('     ')

#Example of the get_balance function
SamJohnson.get_balance()

#Example of the deposit function
SamJohnson.deposit(6.53)

#Example of the withdraw function
SamJohnson.widthdraw(600)

#Example of adding interest
SamJohnson.add_interest()

#Prints balance once again.
SamJohnson.get_balance()

print('    ')
#Below are the reciepts of the four bank accounts that I initialized
SamJohnson.print_receipt()

RickJameson.print_receipt()

JaneDoe.print_receipt()

JohnDoe.print_receipt()
