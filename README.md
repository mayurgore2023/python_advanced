
## demonstration of normal Vs lambda function


#Normal function / Named function:
def Add(no1,no2):
    return no1+no2

# Lambda function /unnamed function:
#syntax= lambda parameter : body
AddFunction = lambda A,B : A+B


# calling of functions
Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function:",Ans1)
print("Addition using lambda function:",Ans2)

