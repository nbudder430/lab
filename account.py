class Account:
    def __init__(self, name: str) -> None:
        """
        This function sets the account name and sets the balance to 0
        :param name: This is the name that will be added to the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> True or False:
        """
        This function takes an amount and adds it to the account balance
        :param amount: This is the amount being deposited into the account, and must be > 0
        :return: Returns True if the transaction was successful, Returns False if not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            self.__account_balance += 0
            return False

    def withdraw(self, amount: float) -> True or False:
        """
        This function takes an amount and subtracts it to the account balance
        :param amount: This is the amount being withdrawn from the account, and must be > 0 and < account balance
        :return: Returns True if the transaction was successful, Returns False if not
        """
        if self.__account_balance >= amount > 0:
            self.__account_balance -= amount
            return True
        else:
            self.__account_balance += 0
            return False

    def get_balance(self):
        """
        This function retrieves the account balance and returns it
        :return: Returns the account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        This function retrieves the account balance and returns it
        :return: Returns the account name
        """
        return self.__account_name
