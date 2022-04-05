class Account:
    def __init__(self, number, owner, balance, limit):
        print(f"building object...{self}")
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    def enquiry(self):
        print(f"Hello {self.__owner}! your balance is: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"Your balance now is: {self.__balance}")

    def withdraw(self, amount):
        if (self.__balance + self.__limit - amount) < 0:
            print(f"Sorry {self.__owner}, you don't have enough balance")
        else:
            self.__balance -= amount
        print(f"Your balance now is: {self.__balance}")
