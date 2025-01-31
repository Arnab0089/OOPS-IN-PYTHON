class BadBankAccount:
    def __init__(self,balance):
        self.balance=balance
    
account1=BadBankAccount(0)

account1.balance=-1

print(account1.balance)


class BankAccount:
    def __init__(self):
        self._balance=0.0

    @property
    def balance(self):
        return self._balance
    
    
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
        else:
            print('Invalid amount')
    
    def withdraw(self,amount):
        if amount>0 and amount<=self._balance:
            self._balance-=amount
        else:
            print('Invalid amount')


account2=BankAccount()
print(account2.balance)

# account2.balance=-1

# print(account2.balance)

account2.deposit(1.99)
print(account2.balance)
account2.withdraw(1.00)
print(account2.balance)