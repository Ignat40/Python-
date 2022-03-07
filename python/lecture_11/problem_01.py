class Person_Identification:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number


class Bank_Account_Wallet:
    def __init__(self, owner:Person_Identification, account_identification: int):
        self.owner = owner
        self.balance = 0.0
        self.account_identification = account_identification

    def deposit(self, amount: float):
        self.balance += amount

    def widthdraw(self, amount: float):
        
        if self.balance > amount:
            self.balance -= amount

        else:
            print("Not enough money...")

    def print_balance(self):
        print("Balance: {", self.balance, "}")


if __name__ == '__main__':

    owner = Person_Identification("Ivan", "Ivanow", "0447250901")
    wallet = Bank_Account_Wallet(owner, 1)
    wallet.deposit(1000)
    wallet.print_balance()
    wallet.widthdraw(755.2)
    wallet.print_balance()




    
