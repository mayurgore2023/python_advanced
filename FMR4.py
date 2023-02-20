
# Demonstration of Filter Map Reduce using normal function:
# filter : even number
# map: addition of 2
# reduce: addition of numbers



from functools import reduce

def EvenChknum(no):
    return (no % 2 ==0)

def Increase(no):
    return no+2

def Add(a,b):
    return a+b

def main():
    arr=[8,9,5,16,2,4,21,30,11]

    #filter
    evenArr=list(filter(EvenChknum,arr))
    print("Data after filter",evenArr)

    #Map
    ModArray=list(map(Increase,evenArr))
    print("data after map:",ModArray)

    #Reduce
    sum= reduce(Add,ModArray)
    print("Data after reduce:",sum)

if __name__=="__main__":
    main()
