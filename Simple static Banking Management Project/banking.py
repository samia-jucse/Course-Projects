class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"

samia = Banking("samia", 10000)
print(f"Account Name: {samia.name}")
print(f"Initial Account Balance: {samia.check_balance()}")
print(f"Balance after Deposit: {samia.deposit(1500)}")
print(f"Balance after Withdrawal: {samia.withdraw(500)}")
print(f"Final Balance: {samia.check_balance()}")
