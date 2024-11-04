class BankAcct:

    def __init__(self, name, account_number, amount=0.0, interest_rate=0.0):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Adjust the interest rate
    def adjust_int_rate(self, new_rate):
        self.interest_rate = int(new_rate)

    # Calculates interest gathered in x days
    def calc_interest(self, days):
        interest = ((self.amount * int(self.interest_rate)) / 100) * (int(days) / 365)
        return interest

    # Deposit funds
    def deposit(self, amount):
        self.amount = int(self.amount) + int(amount)
        print(" ")
        print("Deposit Success!")
        print(f"New Balance: {self.amount}")

    # Withdraw funds
    def withdraw(self, amount):

        # Fails to withdraw
        if int(amount) > int(self.amount):
            print(" ")
            print("Error: Insufficent funds")

        # Withdraw is successful
        else:
            self.amount = int(self.amount) - int(amount)
            print(" ")
            print("Withdraw Successful!")
            print(f"Remaining Balance: {self.amount}")

    # returns balance
    def return_balance(self):
        return self.amount

    # returns account details
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: {self.amount}\n"
                f"Interest Rate: {self.interest_rate}%")

def bank_test():
    account = BankAcct("Billy Bob", "123456789", 110000, 3.0)

    print(account)

    print(" ")
    withdraw_funds = input("Withdraw amount: ")
    account.withdraw(withdraw_funds)

    print(" ")
    deposit_funds = input("Desposit amount: ")
    account.deposit(deposit_funds)

    print(" ")
    rate_new = input("New interest rate: ")
    account.adjust_int_rate(rate_new)

    print(" ")
    time = int(input("Calculate interest for how many days: "))
    interest = account.calc_interest(time)
    print(f"Interest earned: {interest:.2f}")

    print(" ")
    print(" ")
    print("New Bank Information:")
    print(account)

bank_test()