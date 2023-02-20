##  Demonstration of Filter Map Reduce using lambda function

from functools import reduce


def main():
    
    Arr = [8, 9, 5, 16, 2, 4, 21, 30, 11]

    EvenArr= list(filter(lambda no:(no % 2 == 0),Arr))
    print("Data after using filter :",EvenArr)

    ModArray= list(map(lambda no : (no +2),EvenArr))
    print("Data after using map :",ModArray)

    sum= reduce(lambda a,b :(a + b),ModArray)
    print(" Data after reduce:",sum)


if __name__=="__main__":
    main()
