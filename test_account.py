from account import *


class Test:
    def setup_method(self):
        self.p1 = Account("John")
        self.p2 = Account("Penny")
        self.p1.deposit(50)
        self.p2.deposit(10)

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == "John"
        assert self.p1.get_balance() == 50
        assert self.p2.get_name() == "Penny"
        assert self.p2.get_balance() == 10

    def test_deposit(self):
        assert self.p1.deposit(15) is True
        assert self.p1.deposit(-15) is False
        assert self.p2.deposit(15) is True
        assert self.p2.deposit(-15) is False

    def test_withdraw(self):
        assert self.p1.withdraw(15) is True
        assert self.p1.withdraw(-15) is False
        assert self.p2.withdraw(15) is False
        assert self.p2.withdraw(-15) is False
