class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        return f"Interest added: {interest}. New balance: {self.balance}"

class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Exceeded overdraft limit"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"


def main():
    savings = SavingsAccount("12345", 1000, 5)
    print(savings.deposit(500))
    print(savings.add_interest())
    print(savings.withdraw(200))

    current = CurrentAccount("67890", 2000, 500)
    print(current.withdraw(2500))
    print(current.withdraw(3000))

if __name__ == "__main__":
    main()