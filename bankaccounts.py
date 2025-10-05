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

    

# giving some predefined accounts in the 

acc1=BankAccount(101,"Prakhar",2400000)
acc2=BankAccount(102,"shreya",1000000)

# an array for storing all the data of the accounts
accounts=[acc1,acc2]


while True:
    print("\n Bank Management System")
    print("1 . Adding New Account")
    print("2 . Deposite Balance")
    print("3 . WithDrawl")
    print("4 .Exit")

    ch=int(input("Enter Your Action:"))

    if ch==1:
        print("\nEnter the following details to add the new account:-")
        tempname=input("Enter a Teporarat name for your account like acc1, acc2:")
        acc_num=int(input("Enter the account number"))
        owner_name=input("Enter Account holder name: ")
        balance=int(input("Enter the initial balance to the account"));
        tempname=BankAccount(acc_num,owner_name,balance)
        accounts.append(tempname)
    
    elif ch==2:
