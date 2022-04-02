class Account():

    def __init__(self, owner, balance):
        """
        constructor for the class Account
        :param owner: a string representing the name of the owner
        :param balance: a float number representing the account balance
        """
        self.balance, self.owner = balance, owner

    def deposit(self, amount):
        """
        deposits an amount larger than 0 into the balance
        :param amount: a float number
        :return: True on success False otherwise
        """
        if amount > 0:
            self.balance += amount
            print("Deposit Accepted")
            print("New balance: {}".format(self.balance))
            return True
        else:
            print("Deposit Failed")
            return False

    def withdraw(self, amount):
        """
        checks if funds are available to withdraw and if so withdraws the amount
        :param amount: a float number
        :return: True if successful and False otherwise
        """
        if amount < self.balance:
            self.balance - amount
            print("Withdrawal Accepted")
            print("New balance: {}".format(self.balance))
            return True
        else:
            print("Funds Unavailable!")
            return False

    def __str__(self):
        """
        string format for the class
        Account owner: 'owner name'
        Account balance: account balance
        :return: a string
        """
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"



acct1 = Account('Jose',100)
print(acct1)
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
print(acct1)