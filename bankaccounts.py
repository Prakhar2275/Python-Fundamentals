class BankAccount:
    def __init__(self,account_num,owner,balance=0):
        self.account_num=account_num
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited",amount,"New Balance:",self.balance)
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("withdrawn: ",amount,"New Balance:",self.balance)

# Creating the objects for accounts

acc1=BankAccount(101,"Prakhar",2400000)
acc2=BankAccount(101,"Shreya",500)

#performing operations

acc1.deposit(1000)
acc1.withdraw(10)
acc2.withdraw(1000)
acc2.deposit(5000)

#printting the accounts final statements after all the operations

print("Account Number",acc1.account_num)
print("Account Balance",acc1.balance)

print("Account Number",acc2.account_num)
print("Account Balance",acc2.balance)
