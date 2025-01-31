class BankAccount:
    MIN_BALANCE = 1000
    def __init__(self,owner,balance=0):
        self.owner=owner
        self._balance=balance

    def deposit(self,amount):
        if amount<0:
            return 'Invalid amount'
        self._balance+=amount
        print(f'{amount} deposited successfully.')
        self.show_balance()

    def show_balance(self):
        if self._is_valid_amount:
            if self._balance<self.MIN_BALANCE:
                print('Your account balance is below the minimum balance.')
            print(f'Your balance is {self._balance}.')
        else:
            print(f'Your balance is {self._balance}.')

    def _is_valid_amount(self,amount):
        return amount>0
    
    def __log_transaction(self,transaction_type,amount):
        print(f'{transaction_type} of {amount} done successfully. New balance is {self._balance}.')

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<=rate<=5
    

account=BankAccount("Alice",500)

account.show_balance()

account.deposit(10000)

# account.__log_transaction('Deposit',10000)

# print(account._is_valid_intereset(5))
print(BankAccount.is_valid_interest_rate(5))
