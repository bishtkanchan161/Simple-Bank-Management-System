class Bank:
    def __init__(self, name, account_no, balance,pin):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        self.pin=pin
    def display_account(self):
        print("Name:",self.name)
        print("Account Number:",self.account_no)
        print("Balance:",self.balance)
        print("Pin number:",self.pin)
    def deposit(self):
        insert_acc_no =int(input("enter account number:"))
        
        if insert_acc_no == self.account_no:
            print("AVAILIBLE")
            print("You have rights to deposit amount.")
            amount = int(input("Enter the Amount:"))
            if amount > 0:
                self.balance += amount
                print("Rupees",amount,("has deposit in your account."))
                print("Updated balance",(self.balance))
            else:
                print("enter valid amount")
                        
        else:
            print("Enter valid Acoount number!")
        




account1=Bank("sahil",3421,10000,1234)
account1.display_account()
account1.deposit()

# account2=Bank("Nikhil",9065,65000,1234)
# account2.display_account()
# account2.deposit()
