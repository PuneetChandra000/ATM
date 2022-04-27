class ATM:
    def __init__(self, pin):
        self.Pin = pin

    def withdrawl(self):
        print("Withdrawn Successfully")

    def balance(self):
        print("Account has $50,000 balance" )    

def sayPincode():
    pin = int(input("Enter your ATM Pin Number : "))

    pin1 = ATM(pin)

    i = int(input("Enter 1 for transaction, Enter 2 to for the balance enquiry : "))
    
    if i == 1 :
        amount = int(input("Enter the amount : "))
        pin1.withdrawl()

    else :
        pin1.balance()
       
        
sayPincode()





