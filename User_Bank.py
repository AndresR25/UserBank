class BankAccount:
    accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"{self.balance}"
        

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self,n,lt,ag):
        self.name=n
        self.lastname=lt
        self.age=ag
        self.account={
            'checking':BankAccount(.03,2000),
            'savings':BankAccount(.02,4000)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self



Andres = User("Andres","Rodriguez","19")
Andres.account['checking'].deposit(1000)

Question=input("Do you want to deposit or withdraw?")
Question2=input("Which account do you want to access: checking or savings: ")

if(Question2=="checking"):
    if(Question=="deposit"):
        deposit1=int(input("How much do you want to deposit?\n"))
        Andres.account['checking'].deposit(deposit1)

    elif(Question=="withdraw"):
        withdraw1=int(input("How much do you want to withdraw?\n"))
        Andres.account['checking'].withdraw(withdraw1)

elif(Question2=='savings'):
    if(Question=="deposit"):
        deposit2=int(input("How much do you want to deposit?\n"))
        Andres.account['savings'].deposit(deposit2)

    elif(Question=="withdraw"):
        withdraw2=int(input("How much do you want to withdraw?\n"))
        Andres.account['savings'].withdraw(withdraw2)

Andres.display_user_balance()