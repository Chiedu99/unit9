#Chiedu Nduka-Eze
#11/11/16
#This simulates an ATM like program that allows you to view the balance, withdraw, and deposit


class Account:
    """This simulates an ATM like program that allows you to view the balance, withdraw, and deposit"""
    def __init__(self, name, accountName, balance=0):
        """This is the account that has the money"""
        self.name = name
        self.accountName = accountName
        self.balance = balance

    def deposit(self, amount):
        """This funtion takes an amount and adds it to your balance"""
        self.balance += amount

    def withdraw(self, amount):
        """This funtion takes an amount and subtracts it from the balance, if not enough in balance it returns false"""
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def showBalance(self):
        """This function shows your current balance"""
        return self.balance

    def __str__(self):
        """This funtion is th eline that is printed out"""
        return self.name + " has $" + str(self.balance) + " in their account"
