# Accept 2 numbers and perform addition and substraction of it:

# how to think for oop:
# Kay karayecha ahe?        -> Behaviours (Functions)
#   Addition ani Substraction

# Te karayeala kay laganar ahe?     -> Characteristics (Data)
#   2 numbers

# Class = Characteristics + Behaviours
# Class = Data (variables) + Functions




class Arithematic:
    # charateristics (variables) No1 & No2
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    # def Add & Sub are behaviours (functions)
    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2

def main():

    # taking values from user:
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    # objcet of class  is created:
    obj =Arithematic(Value1,Value2)

    # cqalling of behaviors(functions) of class :
    Ans = obj.Add()
    print("Addition is : ",Ans)

    Ans = obj.Sub()
    print("Substraction is : ",Ans)
    
if __name__ == "__main__":
    main()
