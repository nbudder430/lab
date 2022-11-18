class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__acount_balance += amount
            return True
        else:
            self.__account_balance += 0
            return False

    def withdraw(self, amount):
        if amount <= self.__account_balance and amount > 0:
            self.__acount_balance -= amount
            return True
        else:
            self.__account_balance += 0
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
