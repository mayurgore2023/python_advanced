
## Q. Accept n numbers from user store in list and display list of that numbers:

class Numbers:
    # instance variables:
    def __init__(self):
        self.Size = 0
        self.Arr = list()
     
    # instance methods:
    def Accept(self):
        print("Enter how many elements you want : ")
        self.Size = int(input())

        print("Please enter the elements")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are : ")
        for i in range(0,self.Size):
            print(self.Arr[i])

def main():
    #class object:
    obj = Numbers()
    
    #calling instance methods:
    obj.Accept()
    obj.Display()

if __name__ == "__main__":
    main()
