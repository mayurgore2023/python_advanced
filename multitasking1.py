
#Q.  Python application which creats two threads named as even and odd.
#    - even thread display even numbers list and odd thread display odd numbers list:


import threading

def Even_Number(No1,No2):
    EvenNumbers = []
    for i in range(No1,No2+1):
        if (i % 2 == 0):
            EvenNumbers.append(i)
    print("List of Even Numbers:", end=" ")
    print(EvenNumbers)

def Odd_Number(No1,No2):
    OddNumbers = []
    for i in range(No1,No2+1):
        if(i % 2 !=0):
            OddNumbers.append(i)
    print("List of Odd Numbers:",end=" ")
    print(OddNumbers)


def main():
    print("separate out Even and Odd number from given range of numbers list:")

    From= int(input("Numbers start from:"))
    upto= int(input("Numbers upto:"))

    even = threading.Thread(target=Even_Number,args=(From,upto,))  # even thread

    odd = threading.Thread(target=Odd_Number, args=(From,upto,))   # odd thread

    even.start()
    odd.start()


if __name__=="__main__":
    main()
