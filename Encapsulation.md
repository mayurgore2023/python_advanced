
## Encapsulation :
#  - binding of characteristics(variables) and behaviours(Methods/functions) together:
#  - for that we have to create class

# create class:
class student:

    # create variable(Characteristics):
    def __init__(self):
        self.name =""
    
    # create methods/functions(behaviours):
    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name


# create object of class:
obj = student()

# calling of methods in class:
obj.setname("Mayur")

name = obj.getname()
print(name)
