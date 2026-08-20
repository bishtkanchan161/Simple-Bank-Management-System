class Bank:
    def __init__(self, name, account_no, balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance
    def display_account(self):
        print("Name:",self.name)
        print("Account Number:",self.account_no)
        print("Balance:",self.balance)
account=Bank("sahil",3421567891,10000)
account.display_account()