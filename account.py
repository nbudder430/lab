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
        Function adds amount to balance
        :param amount: Amount to Add
        :return: True or False
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> True or False:
        """
        Function subtracts amount from balance
        :param amount: Amount to Subtract
        :return: True or False
        """
        if self.__account_balance >= amount and amount > 0:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to give Account Balance
        :return: Account Balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to give Account Name
        :return: Account Name
        """
        return self.__account_name
