class Atm(object):
    def __init__(self,CardNumber,PIN):
        self.CardNumber = CardNumber
        self.PIN = PIN
    
    def CashWithdrawal(self,CardNumber,PIN,Amount):
        print('You have successfully withdrawed ₹'+ str(Amount)+'!')
    def CashDeposit(self,CardNumber,PIN,Amount):
        print('You have successfully deposited ₹'+ str(Amount)+'!')

# Define some Users
john = Atm(123456789,123)
jane = Atm(987654321,321)

# Methods

print(john.CashWithdrawal(123456789,123,200))
print(jane.CashDeposit(987654321,321,200))

