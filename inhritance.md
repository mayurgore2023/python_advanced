# single inheritance:# we can call the both method in class A and B by creating only obj of class B


# classes:
class A :
    def displayA(self):
        print('welcome to A')

# inherit the class A into class B:
class B (A):
    def displayB(self):
        print('welcome to B')

# make object of class B
obj = B()

# calling of object B:
obj.displayB()

print("-------------------------------------------------------------------------------------------------------)



# Multuple inheritance: we can call the  methods in class A , B and  C by inherit both class A and B in class C

# Classes:
class A :
    def displayA(self):
        print('welcome to A')

class B ():
    def displayB(self):
        print('welcome to B')


# inherit the A and B in class c
class C (A,B):       
    def displayC(self):
        print( 'Welcome to C')
        
# make object of class C:
obj = C()

# calling of object of C:
obj.displayC()

print("-------------------------------------------------------------------------------------------------------)


# Multilevel inheritance: # we can call the both method in class A , B and C by creating only obj of C 
# ( by inherit method of class A in class B and then class B inherit into class c )

# classes:
class A :
    def displayA(self):
        print('welcome to A')

# inherit class A into class B:
class B (A):
    def displayB(self):
        print('welcome to B')

# inherit class B into class C:
class C (B):
    def displayC(self):
        print( 'Welcome to C')
        
# make object of class C:
obj = C()


# calling object of C:
obj.displayC()








