

## user defined FMR functions:
#-- we use it as a module
# Helper_Function : use your function that you  have to perform particular operation
# Data : provide data on which operation will be perform

   


# filter function
def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if (Helper_Function(No) == True):
            Result.append(No)

    return Result

# map function :
def mapX(Helper_Function, Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)

    return Result
    
    
  # reduce function: 
def reduceX(Helper_Function, Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans, no)

    return Ans

