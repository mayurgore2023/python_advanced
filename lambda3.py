
#Q Appliccatopn for finding odd or even number using lambda function

def main():
    No = int(input("please enter the number:"))


    Even = lambda No: No % 2 == 0


    if (Even == True):
        print("{} is even".format(No))
    else:
        print(" {} is odd".format(No))


if __name__=="__main__":
    main()
