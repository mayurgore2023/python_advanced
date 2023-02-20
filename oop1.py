
### Banking Application: create bank account

# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class variable : Bank_Name ,ROI_On_FD
# Class method : DisplayBankInformation
# Static method : DisplayKYCInfo

class Bank_Account:
    
    # creating class varibles:
    Bank_Name = "HDFC Bank PVT LTD"
    ROI = 6.7
    
    # Creating instance variables:
    def __init__(self):
        self.Name = " "
        self.Amount = 0
        self.Address = " "
        self.AccountNo = 0
        
    # Creating instance method
    def CreatAccount(self):
        print("Enter Your Name:")
        self.Name = input()

        print("Enter your initial ammount:")
        self.Amount = int(input())

        print("Enter your Address:")
        self.Address = input()

        print("Enter your Account Number:")
        self.AccountNo = int(input())


    def DisplayAccountInfo(self):
        print("--------Your Account information below------------")

        print("Name of account holder",self.Name)
        print("Account Number:",self.AccountNo)
        print("Address:",self.Address)
        print("Current Account Balance:",self.Amount)
     
    # Create class method:
    @classmethod
    def DisplayBankInfo(cls):
        print("Welcome to banking console")
        print("Name of our bank is:",cls.Bank_Name)
        print("ROI:",cls.ROI)
    
    # Create static method:
    @staticmethod
    def DisplayKYCinfo():
        print("Please consider below KYC information")
        print("According to the rules of Goverment of India you have to submit below documnets")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")


def main():

    Bank_Account.DisplayKYCinfo()

    print("Name of BAnk:",Bank_Account.Bank_Name)
    print("Rate of interest:",Bank_Account.ROI)


    Bank_Account.DisplayBankInfo()
    
    # Creating of class objects:
    User1 = Bank_Account()
    User2 = Bank_Account()



    print("Creating first account:")
    User1.CreatAccount()

    print("Creat second account:")
    User2.CreatAccount()
    
    
    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__=="__main__":
    main()


